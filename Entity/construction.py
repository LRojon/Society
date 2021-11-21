import sys
sys.path.append('..')
import uuid
from utils import Point, rand
from typing import Dict


class TypeConstruction:
    def __init__(self, type: str) -> None:
        if type == "Food":
            self.name = "Restaurant"
            self.color = "#ff7f00"
            self.symbol = "F"
            self.need = "Food"
        elif type == "Water":
            self.name = "Bar"
            self.color = "#0000ff"
            self.symbol = "W"
            self.need = "Water"
        elif type == "Social":
            self.name = "Forum"
            self.color = "#f9e4b7"
            self.symbol = "S"
            self.need = "Social"
        elif type == "Health":
            self.name = "Hôpital"
            self.color = "#ff0000"
            self.symbol = "H"
            self.need = "Health"
        elif type == "Construction":
            self.name = "Chantier"
            self.color = "#888888"
            self.symbol = "C"
            self.need = None
        elif type == "Road":
            self.name = 'Route'
            self.color = "#ffffff"
            self.symbol = "·"
            self.need = None


class Construction:
    def __init__(self, type: str, x: int, y: int, cost: Dict[str, int]) -> None:
        self.uid = str(uuid.uuid4())
        self.position = Point(x, y)
        self.cost = cost
        if type == "Food":
            self.nbHMax = 5
            self.nbH = 0
            self.type = TypeConstruction(type)
        elif type == "Water":
            self.nbHMax = 5
            self.nbH = 0
            self.type = TypeConstruction(type)
        elif type == "Social":
            self.nbHMax = 5
            self.nbH = 0
            self.type = TypeConstruction(type)
        elif type == "Health":
            self.nbHMax = 5
            self.nbH = 0
            self.type = TypeConstruction(type)
        elif type == "Construction":
            self.nbHMax = 5
            self.nbH = 0
            self.type = TypeConstruction(type)
        elif type == "Road":
            self.nbHMax = 1
            self.nbH = 0
            self.type = TypeConstruction(type)

    def toString(self):
        ret = "uid : " + self.uid + "\n"
        ret += "position : " + str(self.position.x) + \
            ", " + str(self.position.y) + "\n"
        ret += "cost : " + str(self.cost) + "\n"
        ret += "type : \n"
        ret += "\tname : " + self.type.name + "\n"
        ret += "\tcolor : " + self.type.color + "\n"
        ret += "\tsymbol : " + self.type.symbol + "\n"
        ret += "\tneed : " + str(self.type.need)
        return ret
