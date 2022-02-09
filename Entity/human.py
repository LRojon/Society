
import sys
import uuid
from copy import deepcopy
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

# setting path


from utils import Point, rand, generateName



class Need :

    # Initialisation
    def __init__(self, name : str, nbMax : int = 100, threshold : int = 25) -> None:
        self.name = name
        self.nbMax = nbMax
        self.nb = nbMax
        self.threshold = threshold

    # Retourne le niveau de besoin actuel
    def getNb(self) -> int:
        return self.nb

    # Modifie le niveau de besoin actuel
    def setNb(self, value : int) -> None:
        if value >= 0 and value <= self.nbMax:
            self.nb = value

    # Baisse le besoin de 1
    def downNeed(self) -> None:
        self.nb = self.nb - 1


class Human :

    # Initialisation
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

    # Generation des noms en 3 parties (2 parents et 1 unique)
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
                
    # Generation des besoins en utilisant ceux des parents
    def generateNeeds(self, list_Needs : list) -> list:
        output = {}
        parents = self.parents
        if parents == []:
            for i in list_Needs:
                need = Need(i, rand(30, 20) )
                output[i] = need
        else :
            for i in list_Needs:
                val1 = parents[0].needs[i].nbMax
                val2 = parents[1].needs[i].nbMax
                avg_parents = (val1 + val2) / 2
                need = Need(i, avg_parents + rand(5, -4) )
                output[i] = need
        return output

    # Création d'un nouveau humain en utilisant un autre humain
    def makeCracCracBoomBoom(self, otherHuman) -> None:
        if rand(100) < 20:
            self.society.alive.append(Human([self, otherHuman] , self))

    # Interaction avec le batiment sur lequel il est
    def interact(self) -> None:
        point = self.position
        place = self.society.map[point.x, point.y]
        if place.symbole == "S":
            otherHuman = place.findPartner(self)
            if otherHuman:
                self.makeCracCracBoomBoom(otherHuman)
        need_update = place.use()
        for i in need_update.keys():
            self.needs[i] = self.needs[i] + need_update[i]

    # Transforme la map en grille binaire (0 = obstacle)
    def transGrille(self) -> list:
        map = deepcopy(self.society.map)
        for i in range(len(map)):
            for j in range(len(map[i])):
                map[i][j] = int(not(map[i][j].isisFull()))
        return map

    # Retourne le prochain mouvement vers l'objectif
    def getPathfinding(self, point: Point) -> Point:
        my_x = self.position.x
        my_y = self.position.y

        grid = Grid(matrix=self.transGrille())

        start = grid.node(my_x, my_y)
        end = grid.node(point.x, point.y)

        finder = AStarFinder()
        path, _ = finder.find_path(start, end, grid)

        if len(path) > 1:
            a, b = path[1]
        else:
            a = self.x
            b = self.y

        return Point(a, b)

    # Déroulement du tour d'un humain. Retourne True si mort.
    def nextTurn(self) -> bool:
        needs = self.needs()
        minVal_need = needs["Water"]
        minName_need = "Water"

        for i in needs.keys():
            if needs[i] < minVal_need:
                minName_need = i
                minVal_need = needs[i]

        if minVal_need == 0:
            return True

        # Prend le premier pour le moment
        point = self.society.needToBuilding[minName_need][0]

        new_position = self.getPathfinding(point)

        self.position = new_position
        
        return False