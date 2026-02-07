# -*- coding: utf-8 -*-
"""Module d'exemple avec documentation Sphinx complète.

Ce module montre comment bien documenter votre code Python
pour qu'il soit automatiquement transformé en belle documentation
par Sphinx.

Example:
    Utilisation basique du module::

        from exemple_sphinx import NavigationLight, calculate_intensity

        # Créer un feu de navigation
        light = NavigationLight(sector="Hune", light_range=2)
        
        # Calculer l'intensité
        intensity = light.get_intensity(angle=0)
        print(f"Intensité: {intensity} cd")

Attributes:
    LIGHT_COLORS (dict): Correspondance secteur → couleur.
    DEFAULT_RANGE (int): Portée par défaut si non spécifiée.

Todo:
    * Ajouter support pour feux clignotants
    * Implémenter validation COLREG complète
    * Ajouter export vers format ISO 8559

.. _COLREG:
   https://www.imo.org/en/About/Conventions/Pages/COLREG.aspx
"""

from typing import Dict, List, Optional, Tuple
import math


# Constantes de module
LIGHT_COLORS: Dict[str, str] = {
    'Hune': 'blanc',
    'Poupe': 'blanc',
    'Bâbord': 'rouge',
    'Tribord': 'vert',
}

DEFAULT_RANGE: int = 2


class NavigationLight:
    """Représente un feu de navigation maritime.
    
    Cette classe modélise un feu de navigation avec ses caractéristiques
    photométriques et colorimétriques selon les normes COLREG.
    
    Args:
        sector: Type de feu ("Hune", "Poupe", "Bâbord", "Tribord").
        light_range: Portée lumineuse (1-6). Default: 2.
        inclination: Angle d'inclinaison en degrés. Default: 0.
        
    Attributes:
        sector (str): Secteur du feu.
        light_range (int): Portée sélectionnée.
        inclination (float): Inclinaison du feu.
        color (str): Couleur réglementaire du feu.
        max_intensity (float): Intensité maximale calculée en candelas.
        
    Raises:
        ValueError: Si le secteur est inconnu ou la portée invalide.
        
    Example:
        >>> light = NavigationLight("Hune", light_range=3)
        >>> light.color
        'blanc'
        >>> light.max_intensity
        15.0
        
        Avec inclinaison (réduit l'intensité de 50%)::
        
            >>> light_inclined = NavigationLight("Bâbord", light_range=2, inclination=10)
            >>> light_inclined.max_intensity
            2.7
            
    Note:
        L'intensité est automatiquement réduite de 50% si une inclinaison
        est détectée (valeur non nulle).
        
    See Also:
        calculate_intensity: Fonction de calcul standalone.
        
    .. versionadded:: 1.0
    
    .. versionchanged:: 1.1
       Ajout du support de l'inclinaison
    """
    
    # Dictionnaire de puissances selon COLREG Annex I
    POWER_TABLE: Dict[int, float] = {
        1: 1.1,
        2: 5.4,
        3: 15.0,
        4: 33.0,
        5: 65.0,
        6: 118.0,
    }
    
    def __init__(
        self,
        sector: str,
        light_range: int = DEFAULT_RANGE,
        inclination: float = 0.0
    ) -> None:
        """Initialise un feu de navigation."""
        if sector not in LIGHT_COLORS:
            raise ValueError(
                f"Secteur inconnu: {sector}. "
                f"Valeurs possibles: {list(LIGHT_COLORS.keys())}"
            )
        
        if light_range not in self.POWER_TABLE:
            raise ValueError(
                f"Portée invalide: {light_range}. "
                f"Doit être entre 1 et 6."
            )
        
        self.sector = sector
        self.light_range = light_range
        self.inclination = inclination
        self.color = LIGHT_COLORS[sector]
        self.max_intensity = self._calculate_max_intensity()
    
    def _calculate_max_intensity(self) -> float:
        """Calcule l'intensité maximale.
        
        Méthode privée qui applique la réduction d'intensité
        si le feu est incliné.
        
        Returns:
            Intensité maximale en candelas.
        """
        base_power = self.POWER_TABLE[self.light_range]
        
        if self.inclination != 0:
            return base_power * 0.5
        
        return base_power
    
    def get_intensity(self, angle: float) -> float:
        """Calcule l'intensité à un angle donné.
        
        Cette méthode retourne l'intensité lumineuse mesurée à un angle
        horizontal spécifique, en tenant compte des zones de conformité
        du secteur.
        
        Args:
            angle: Angle horizontal en degrés (-180 à +180).
                   0° représente l'avant du navire.
                   
        Returns:
            Intensité lumineuse en candelas à cet angle.
            Retourne 0 si l'angle est hors du secteur autorisé.
            
        Raises:
            ValueError: Si l'angle est hors de la plage [-180, 180].
            
        Example:
            >>> light = NavigationLight("Tribord", light_range=2)
            >>> light.get_intensity(45)  # 45° tribord
            5.4
            >>> light.get_intensity(-45)  # 45° bâbord (hors secteur)
            0.0
            
        Note:
            La distribution de l'intensité dépend des zones définies
            par le secteur selon COLREG.
            
        Warning:
            Cette méthode ne prend pas en compte l'angle vertical.
            Pour une analyse 3D complète, utilisez :meth:`get_intensity_3d`.
        """
        # Normaliser l'angle
        if not -180 <= angle <= 180:
            raise ValueError(f"Angle hors limites: {angle}. Doit être entre -180 et 180.")
        
        # Simplification: retourne intensité max si dans le secteur
        # (implémentation complète nécessiterait les zones détaillées)
        if self._is_in_sector(angle):
            return self.max_intensity
        
        return 0.0
    
    def _is_in_sector(self, angle: float) -> bool:
        """Vérifie si l'angle est dans le secteur autorisé.
        
        Args:
            angle: Angle en degrés.
            
        Returns:
            True si l'angle est dans le secteur, False sinon.
        """
        # Implémentation simplifiée
        sector_ranges = {
            'Hune': (-180, 180),
            'Poupe': (112.5, 247.5),
            'Bâbord': (-112.5, 0),
            'Tribord': (0, 112.5),
        }
        
        min_angle, max_angle = sector_ranges[self.sector]
        return min_angle <= angle <= max_angle
    
    def get_chromaticity(self) -> Tuple[float, float]:
        """Retourne les coordonnées chromatiques (x, y) du feu.
        
        Coordonnées dans le système CIE 1931 pour la couleur
        réglementaire du feu.
        
        Returns:
            Tuple (x, y) des coordonnées chromatiques.
            
        Example:
            >>> light = NavigationLight("Bâbord", light_range=2)
            >>> x, y = light.get_chromaticity()
            >>> print(f"Rouge: x={x:.3f}, y={y:.3f}")
            Rouge: x=0.700, y=0.290
            
        Note:
            Les valeurs retournées sont des valeurs typiques.
            Les vraies valeurs doivent être mesurées pour chaque feu.
        """
        # Coordonnées CIE 1931 typiques
        chromaticity_coords = {
            'blanc': (0.310, 0.316),
            'rouge': (0.700, 0.290),
            'vert': (0.150, 0.450),
        }
        
        return chromaticity_coords[self.color]
    
    def __repr__(self) -> str:
        """Représentation textuelle du feu.
        
        Returns:
            Chaîne décrivant le feu.
        """
        return (
            f"NavigationLight(sector={self.sector!r}, "
            f"range={self.light_range}, "
            f"color={self.color!r}, "
            f"max_intensity={self.max_intensity} cd)"
        )


def calculate_intensity(
    light_range: int,
    angle: float,
    inclination: float = 0.0
) -> float:
    """Calcule l'intensité lumineuse pour des paramètres donnés.
    
    Fonction utilitaire pour calculer rapidement une intensité
    sans créer d'objet NavigationLight.
    
    Args:
        light_range: Portée du feu (1-6).
        angle: Angle horizontal en degrés.
        inclination: Angle d'inclinaison. Default: 0.
        
    Returns:
        Intensité calculée en candelas.
        
    Raises:
        ValueError: Si les paramètres sont invalides.
        
    Example:
        Calcul simple::
        
            >>> intensity = calculate_intensity(light_range=2, angle=0)
            >>> print(f"{intensity} cd")
            5.4 cd
            
        Avec inclinaison::
        
            >>> intensity = calculate_intensity(
            ...     light_range=3,
            ...     angle=45,
            ...     inclination=10
            ... )
            >>> print(f"{intensity} cd")
            7.5 cd
            
    See Also:
        NavigationLight: Classe complète pour la modélisation.
        
    .. deprecated:: 1.2
       Utilisez plutôt la classe NavigationLight pour une API complète.
    """
    if light_range not in NavigationLight.POWER_TABLE:
        raise ValueError(f"Portée invalide: {light_range}")
    
    base = NavigationLight.POWER_TABLE[light_range]
    
    if inclination != 0:
        base *= 0.5
    
    # Simplification: angle non pris en compte dans cette version
    return base


def get_sector_angles(sector: str) -> Dict[str, float]:
    """Retourne les angles limites d'un secteur.
    
    Args:
        sector: Nom du secteur.
        
    Returns:
        Dictionnaire avec 'min_angle' et 'max_angle'.
        
    Example:
        >>> angles = get_sector_angles("Tribord")
        >>> angles
        {'min_angle': 0, 'max_angle': 112.5}
        
    Raises:
        KeyError: Si le secteur n'existe pas.
    """
    angles = {
        'Hune': {'min_angle': -180, 'max_angle': 180},
        'Poupe': {'min_angle': 112.5, 'max_angle': 247.5},
        'Bâbord': {'min_angle': -112.5, 'max_angle': 0},
        'Tribord': {'min_angle': 0, 'max_angle': 112.5},
    }
    
    return angles[sector]


if __name__ == "__main__":
    # Exemple d'utilisation
    import doctest
    doctest.testmod(verbose=True)
    
    # Démonstration
    print("=== Démonstration ===\n")
    
    light = NavigationLight("Hune", light_range=3, inclination=5)
    print(light)
    print(f"Intensité à 0°: {light.get_intensity(0)} cd")
    
    x, y = light.get_chromaticity()
    print(f"Chromaticité: ({x}, {y})")
