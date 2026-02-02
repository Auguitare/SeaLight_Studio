import tkinter as tk

zone_limite_1 = dict()
zone_limite_2 = dict()
zone_limite_3 = dict()

def intensity_calc(range, inclinaison):
    global zone_limite_1, zone_limite_2, zone_limite_3
    match range:
        case 1:
            max_power = 1.1
        case 2:
            max_power = 5.4
        case 3:
            max_power = 15
        case 4:
            max_power = 33
        case 5:
            max_power = 65
        case 6:
            max_power = 118
        case _:
            tk.messagebox.showwarning("Avertissement", "choisir une portée.")

    if(inclinaison != 0):
        max_power *= 0.5

    zone_limite_1 ["y"]= [0.1*max_power, max_power, max_power, 0.1*max_power, 0.1*max_power]
    zone_limite_2 ["y"]= [0, 0.5*max_power, 0.5*max_power, max_power, max_power, 0.5*max_power, 0.5*max_power, 0, 0]
    zone_limite_3 ["y"]= [max_power, 0.1*max_power, 0.1*max_power, max_power, max_power]

def hune(range, inclinaison):
    global zone_limite_1, zone_limite_2, zone_limite_3

    intensity_calc(range, inclinaison)
    
    zone_limite_1 ["x"]= [-132.5, -132.5, -117.5, -117.5, -132.5]
    zone_limite_2 ["x"]= [-112.5, -112.5, -107.5, -107.5, 107.5, 107.5, 112.5, 112.5, -112.5]
    zone_limite_3 ["x"]= [132.5, 132.5, 117.5, 117.5, 132.5]


def poupe(range, inclinaison):
    global zone_limite_1, zone_limite_2, zone_limite_3

    intensity_calc(range, inclinaison)
    
    zone_limite_1 ["x"]= [85, 85, 107.5, 107.5, 85]
    zone_limite_2 ["x"]= [112.5, 112.5, 117.5, 117.5, 242.5, 242.5, 247.5, 247.5, 112.5]
    zone_limite_3 ["x"]= [267.5, 267.5, 252.5, 252.5, 267.5]


def babord(range, inclinaison):
    global zone_limite_1, zone_limite_2, zone_limite_3

    intensity_calc(range, inclinaison)
    
    zone_limite_1 ["x"]= [-30, -30, -3, -3, -30]
    zone_limite_2 ["x"]= [0, 0, 0, 0, 107.5, 107.5, 112.5, 112.5, 0]
    zone_limite_3 ["x"]= [142.5, 142.5, 117.5, 117.5, 142.5]


def tribord(range, inclinaison):
    global zone_limite_1, zone_limite_2, zone_limite_3

    intensity_calc(range, inclinaison)
    
    zone_limite_1 ["x"]= [-142.5, -142.5, -117.5, -117.5, -142.5]
    zone_limite_2 ["x"]= [-112.5, -112.5, -107.5, -107.5, 0, 0, 0, 0, -112.5]
    zone_limite_3 ["x"]= [30, 30, 3, 3, 30]


def only_value():
    global zone_limite_1, zone_limite_2, zone_limite_3

    zone_limite_1 = {
        "x": [0],
        "y": [0],
    }

    zone_limite_2 = {
        "x": [0],
        "y": [0],
    }

    zone_limite_3 = {
        "x": [0],
        "y": [0],
    }
