import random
import json
import curses
from numpy.random import default_rng

class Point :
    def __init__(self, x : int = -1, y : int = -1) -> None:
        self.x = x
        self.y = y

def rand(max : int, min : int = 0) -> int:
    random.seed()
    return random.randint(min, max)

def randDice(formula : str) -> int:
    res = 0
    if "+" in formula:
        res = int(formula.split('+')[1])
    nbDice = int(formula.split('d')[0])
    nbFace = int(formula.split('d')[1].split('+')[0])
    for i in range(0, nbDice):
        res += rand(nbFace, 1)
    return res

def generateName(nb : int = 3):
    list_voyelle = list("aeiouy")
    list_consonne = list("bcdfghjklmnpqrstvwxz")
    rng = default_rng()
    voyelles = rng.choice(list_voyelle, size = nb)
    consonnes = rng.choice(list_consonne, size = nb)
    vals = [consonnes[i] + voyelles[i] for i in range(nb)]
    return "-".join(vals)
