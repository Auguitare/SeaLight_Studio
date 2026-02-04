import tkinter as tk

def intensity_calc(range, inclinaison):
    max_power = 0
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

    return {
        1: {"Y": [0.1*max_power, max_power, max_power, 0.1*max_power, 0.1*max_power]},
        2: {"Y": [0, 0.5*max_power, 0.5*max_power, max_power, max_power, 0.5*max_power, 0.5*max_power, 0, 0]},
        3: {"Y": [max_power, 0.1*max_power, 0.1*max_power, max_power, max_power]}
    }


def hune(range, inclinaison):
    zone = intensity_calc(range, inclinaison)
    
    zone[1]["X"]= [-132.5, -132.5, -117.5, -117.5, -132.5]
    zone[2]["X"]= [-112.5, -112.5, -107.5, -107.5, 107.5, 107.5, 112.5, 112.5, -112.5]
    zone[3]["X"]= [132.5, 132.5, 117.5, 117.5, 132.5]

    return zone


def poupe(range, inclinaison):
    zone = intensity_calc(range, inclinaison)
    
    zone[1]["X"]= [85, 85, 107.5, 107.5, 85]
    zone[2]["X"]= [112.5, 112.5, 117.5, 117.5, 242.5, 242.5, 247.5, 247.5, 112.5]
    zone[3]["X"]= [267.5, 267.5, 252.5, 252.5, 267.5]

    return zone


def babord(range, inclinaison):

    zone = intensity_calc(range, inclinaison)
    
    zone[1]["X"]= [-30, -30, -3, -3, -30]
    zone[2]["X"]= [0, 0, 0, 0, 107.5, 107.5, 112.5, 112.5, 0]
    zone[3]["X"]= [142.5, 142.5, 117.5, 117.5, 142.5]

    return zone


def tribord(range, inclinaison):

    zone = intensity_calc(range, inclinaison)
    
    zone[1]["X"]= [-142.5, -142.5, -117.5, -117.5, -142.5]
    zone[2]["X"]= [-112.5, -112.5, -107.5, -107.5, 0, 0, 0, 0, -112.5]
    zone[3]["X"]= [30, 30, 3, 3, 30]

    return zone


def only_value():
    zone = {}
    zone[1] = {"X": [], "Y": []}
    zone[2] = {"X": [], "Y": []}
    zone[3] = {"X": [], "Y": []}

    zone[1]["X"] = [0]
    zone[1]["Y"] = [0]
    zone[2]["X"] = [0]
    zone[2]["Y"] = [0]
    zone[3]["X"] = [0]
    zone[3]["Y"] = [0]

    return zone
