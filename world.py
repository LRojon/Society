from typing import List
from Entity.society import Society
from utils import Point, rand


class World:
    def __init__(self, width : int, height : int, societies : List[Society]) -> None:
        self.size = Point(width, height)
        self.societies = societies
        self.map = [[None for j in range(height)] for i in range(width)]
        for society in self.societies:
            ox_s = rand(width)
            oy_s = rand(height)
            while not self.isInSociety(ox_s, oy_s):
                ox_s = rand(width)
                oy_s = rand(height)
            society.genMap(0, 0, self.size.x, self.size.y)
            
    def isInSociety(self, x : int, y : int) -> bool:
        ret = False
        for society in self.societies:
            width_s = len(society.map[0])
            height_s = len(society.map)
            if society.origin.x - width_s // 2 <= x and x <= society.origin.x + width_s // 2 and society.origin.y - height_s // 2 <= y and y <= society.origin.y + height_s // 2:
                ret = True
        return ret
    
    def printWorld() -> None:
        pass
    
    def nextTurn() -> None:
        pass
    
    # Fusionne les map des S dans self.map
    def updateMap() -> None:
        pass
                