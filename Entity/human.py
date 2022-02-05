
import sys
import uuid

# setting path
sys.path.append('..')

from utils import Point, rand, generateName
#from society import Society



class Need :

    def __init__(self, name : str, nbMax : int = 100, threshold : int = 25) -> None:
        self.name = name
        self.nbMax = nbMax
        self.nb = nbMax
        self.threshold = threshold

    def getNb(self) -> int:
        return self.nb

    def setNb(self, value : int) -> None:
        if value >= 0 and value <= self.nbMax:
            self.nb = value

    def downNeed(self) -> None:
        self.nb = self.nb - 1


class Human :

    def __init__(self, parents : list = [], society = None) -> None:
        self.uid = str(uuid.uuid4())
        self.society = society
        self.parents = parents
        self.name = self.generateName()
        self.nbTurn = 0
        self.sex = True if rand(1) == 1 else False
        self.position = Point()
        list_Needs = ["Water", "Food", "Health", "Social"]
        self.needs = self.generateNeeds(list_Needs)

    def generateName(self):
        parents = self.parents
        if parents == []:
            name = generateName(3)
        else:
            name = generateName(1) + "-"
            for i in parents:
                name += i.name.split("-")[2] + "-"
            name = name[:-1]
        return name
                

    def generateNeeds(self, list_Needs : list) -> list:
        output = []
        for i in list_Needs:
            need = Need(i, rand(100, 70))
            output.append(need)
        return output

    # False si vivant 
    def nextTurn(self) -> bool:
        return False

    # Suivant proba et besoins insert H in S
    def makeCracCracBoomBoom(self) -> None:
        pass

    # Interaction avec env
    def interact(self) -> None:
        pass

    # Return next point 
    def getPathfinding(self, x : int , y : int) -> Point:
        return Point()