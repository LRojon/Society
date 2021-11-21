import sys

from human import Human

# setting path
sys.path.append('..')

from utils import generateName, rand, Point


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

    def __init__(self, name: str = "", nbInitH: int = 5) -> None:
        self.name = name if name != "" else generateName(5)
        self.nbInitH = nbInitH
        self.alive = list()
        for i in range(nbInitH):
            self.alive.append(Human())
        self.dead = list()
        self.origin = Point()
        self.map = []

    def updateMap(self) -> None:
        pass

    def nextTurn(self) -> None:
        pass

    def printHumans(self):
        for i in self.alive:
            print("My name is ", i.name)
                
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


s = Society()
s.genMap(3,3)