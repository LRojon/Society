import sys

# setting path
sys.path.append('..')

from Entity.human import Human
from utils import generateName, rand, Point

'''
V = Vide
R = Route
H = Hopital
F = Food
W = Water
C = Construction
S = Social
U = Unknow
'''


map_society = [
    ["V", "V", "V", "V", "V", "V", "V"],
    ["V", "V", "R", "F", "R", "V", "V"],
    ["V", "R", "R", "R", "R", "R", "V"],
    ["V", "H", "R", "S", "R", "W", "V"],
    ["V", "R", "R", "R", "R", "R", "V"],
    ["V", "V", "R", "C", "R", "V", "V"],
    ["V", "V", "V", "V", "V", "V", "V"]
]


class Society:

    # Initialisation
    def __init__(self, name: str = "", nbInitH: int = 5) -> None:
        self.name = name if name != "" else generateName(5)
        self.nbInitH = nbInitH
        self.alive = list()
        for _ in range(nbInitH):
            self.alive.append(Human([] , self))
        self.dead = list()
        self.origin = Point()
        self.map = []
        self.needToBuilding = {}

    # Génération d'une map qui fait matcher les besoins avec la position des batiments qui le remplissent
    def generateNeedToBuilding(self) -> dict:
        dic = {}
        map = self.map
        
        for i in len(map):
            for j in len(map[0]):
                typeBuilding = str(type(map[i][j]))
                if typeBuilding != "Road" and typeBuilding != "Construction":
                    dic[typeBuilding].append(map[i][j].position)

        return dic

    # TODO
    # Mise à disposition de la map global dans la society
    def updateMap(self) -> None:
        # update map
        self.needToBuilding = self.generateNeedToBuilding()
        pass

    # TODO
    # Déroulement du tour de la society et des humains
    def nextTurn(self) -> None:
        pass

    # Ecriture du nom des humains vivant de la society
    def printHumans(self):
        for i in self.alive:
            print("My name is ", i.name, " | My position is [", i.position.x , ",", i.position.y, "]")

    
    # Calcage de la society sur la map entière avec point central et dimension            
    def genMap(self,  originX: int, originY: int, width: int = 7, height: int = 7) -> None:
        height_s = len(map_society)
        width_s = len(map_society[0])
        if originX * originY >= 0 and width >= originX + width_s//2 and height >= originY + height_s//2 and originY - height_s//2 >= 0 and originX - width_s//2 >= 0:
            self.origin = [originX, originY]
            map = [["U" for j in range(height)] for i in range(width)]
            for x in range(0, height_s):
                for y in range(0, width_s):
                    map[originX - width_s//2 + x][originY - height_s//2 + y] = map_society[x][y]
            self.map = map
            for i in self.alive:
                i.position = Point(originX, originY)
        else:
            print("ERROR")

    def printMap(self):
        map = self.map
        for i in range(len(map)):
            s = ""
            for j in range(len(map[0])):
                s = s + " " + map[i][j]
            print(s)
