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





## à garder au cas où
    # def poupe_0():
    #     global zone_limite_1, zone_limite_2, zone_limite_3

    #     # Secteur interdit 1
    #     zone_limite_1 = {"x": [85, 85, 107.5, 107.5, 85], "y": [1.5, 15, 15, 1.5, 1.5]}

    #     # Secteur interdit 2
    #     zone_limite_2 = {
    #         "x": [112.5, 112.5, 117.5, 117.5, 242.5, 242.5, 247.5, 247.5, 112.5],
    #         "y": [0, 7.5, 7.5, 15, 15, 7.5, 7.5, 0, 0],
    #     }

    #     # Secteur interdit 3
    #     zone_limite_3 = {
    #         "x": [267.5, 267.5, 252.5, 252.5, 267.5],
    #         "y": [15, 1.5, 1.5, 15, 15],
    #     }

    # def hune_0():
    #     global zone_limite_1, zone_limite_2, zone_limite_3

    #     zone_limite_1 = {
    #         "x": [-132.5, -132.5, -117.5, -117.5, -132.5],
    #         "y": [6.5, 118, 118, 6.5, 6.5],
    #     }

    #     zone_limite_2 = {
    #         "x": [-112.5, -112.5, -107.5, -107.5, 107.5, 107.5, 112.5, 112.5, -112.5],
    #         "y": [0, 59, 59, 118, 118, 59, 59, 0, 0],
    #     }

    #     zone_limite_3 = {
    #         "x": [132.5, 132.5, 117.5, 117.5, 132.5],
    #         "y": [118, 6.5, 6.5, 118, 118],
    #     }


    # def hune_25():
    #     global zone_limite_1, zone_limite_2, zone_limite_3

    #     zone_limite_1 = {
    #         "x": [-132.5, -132.5, -117.5, -117.5, -132.5],
    #         "y": [6.5, 59, 59, 6.5, 6.5],
    #     }

    #     zone_limite_2 = {
    #         "x": [-112.5, -112.5, -107.5, -107.5, 107.5, 107.5, 112.5, 112.5, -112.5],
    #         "y": [0, 29.5, 29.5, 59, 59, 29.5, 29.5, 0, 0],
    #     }

    #     zone_limite_3 = {
    #         "x": [132.5, 132.5, 117.5, 112.5, 132.5],
    #         "y": [59, 6.5, 6.5, 59, 59],
    #     }


    # def poupe_0():
    #     global zone_limite_1, zone_limite_2, zone_limite_3

    #     # Secteur interdit 1
    #     zone_limite_1 = {"x": [85, 85, 107.5, 107.5, 85], "y": [1.5, 5.4, 5.4, 1.5, 1.5]}

    #     # Secteur interdit 2
    #     zone_limite_2 = {
    #         "x": [112.5, 112.5, 117.5, 117.5, 242.5, 242.5, 247.5, 247.5, 112.5],
    #         "y": [0, 2.7, 2.7, 5.4, 5.4, 2.7, 2.7, 0, 0],
    #     }

    #     # Secteur interdit 3
    #     zone_limite_3 = {
    #         "x": [267.5, 267.5, 252.5, 252.5, 267.5],
    #         "y": [5.4, 1.5, 1.5, 5.4, 5.4],
    #     }


    # def poupe_25():
    #     global zone_limite_1, zone_limite_2, zone_limite_3

    #     zone_limite_1 = {
    #         "x": [92.5, 92.5, 107.5, 107.5, 92.5],
    #         "y": [1.5, 7.5, 7.5, 1.5, 1.5],
    #     }

    #     zone_limite_2 = {
    #         "x": [112.5, 112.5, 117.5, 117.5, 242.5, 242.5, 247.5, 247.5, 112.5],
    #         "y": [0, 3.75, 3.75, 7.5, 7.5, 3.75, 3.75, 0, 0],
    #     }

    #     zone_limite_3 = {
    #         "x": [267.5, 267.5, 252.5, 252.5, 267.5],
    #         "y": [7.5, 1.5, 1.5, 7.5, 7.5],
    #     }


    # def babord_0():
    #     global zone_limite_1, zone_limite_2, zone_limite_3

    #     zone_limite_1 = {
    #         "x": [-30, -30, -3, -3, -30],
    #         "y": [1.5, 15, 15, 1.5, 1.5],
    #     }

    #     zone_limite_2 = {
    #         "x": [0, 0, 0, 0, 107.5, 107.5, 112.5, 112.5, 0],
    #         "y": [0, 7.5, 7.5, 15, 15, 7.5, 7.5, 0, 0],
    #     }

    #     zone_limite_3 = {
    #         "x": [142.5, 142.5, 117.5, 117.5, 142.5],
    #         "y": [15, 1.5, 1.5, 15, 15],
    #     }


    # def babord_25():
    #     global zone_limite_1, zone_limite_2, zone_limite_3

    #     zone_limite_1 = {
    #         "x": [-30, -30, -3, -3, -30],
    #         "y": [1.5, 7.5, 7.5, 1.5, 1.5],
    #     }

    #     zone_limite_2 = {
    #         "x": [0, 0, 0, 0, 107.5, 107.5, 112.5, 112.5, 0],
    #         "y": [0, 3.75, 3.75, 7.5, 7.5, 3.75, 3.75, 0, 0],
    #     }

    #     zone_limite_3 = {
    #         "x": [142.5, 142.5, 117.5, 117.5, 142.5],
    #         "y": [7.5, 1.5, 1.5, 7.5, 7.5],
    #     }


    # def tribord_0():
    #     global zone_limite_1, zone_limite_2, zone_limite_3

    #     zone_limite_1 = {
    #         "x": [-142.5, -142.5, -117.5, -117.5, -142.5],
    #         "y": [1.5, 15, 15, 1.5, 1.5],
    #     }

    #     zone_limite_2 = {
    #         "x": [-112.5, -112.5, -107.5, -107.5, -5, -5, 0, 0, -112.5],
    #         "y": [0, 7.5, 7.5, 15, 15, 7.5, 7.5, 0, 0],
    #     }

    #     zone_limite_3 = {
    #         "x": [30, 30, 5, 5, 30],
    #         "y": [15, 1.5, 1.5, 15, 15],
    #     }


    # def tribord_25():
    #     global zone_limite_1, zone_limite_2, zone_limite_3

    #     zone_limite_1 = {
    #         "x": [-142.5, -142.5, -117.5, -117.5, -142.5],
    #         "y": [1.5, 7.5, 7.5, 1.5, 1.5],
    #     }

    #     zone_limite_2 = {
    #         "x": [-112.5, -112.5, -107.5, -107.5, -5, -5, 0, 0, -112.5],
    #         "y": [0, 3.75, 3.75, 7.5, 7.5, 3.75, 3.75, 0, 0],
    #     }

    #     zone_limite_3 = {
    #         "x": [30, 30, 5, 5, 30],
    #         "y": [7.5, 1.5, 1.5, 7.5, 7.5],
    #     }


    # def only_value():
    #     global zone_limite_1, zone_limite_2, zone_limite_3

    #     zone_limite_1 = {
    #         "x": [0],
    #         "y": [0],
    #     }

    #     zone_limite_2 = {
    #         "x": [0],
    #         "y": [0],
    #     }

    #     zone_limite_3 = {
    #         "x": [0],
    #         "y": [0],
    #     }

