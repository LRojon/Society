from typing import List
from Entity.society import Society
from utils import Point, rand
import curses


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
    
    # Methode test de curses
    @staticmethod
    def printWorld() -> None:
        screen = curses.initscr()
        #curses.curs_set(0)
        curses.start_color()
        curses.use_default_colors()

        curses.init_pair(1  , curses.COLOR_BLACK,   curses.COLOR_WHITE)
        for i in range(1, 255):
            curses.init_pair(i + 1, i, -1)
        HUMAN = 0
        FOOD = 95
        WATER = 10
        SOCIAL = 211
        HEALTH = 197
        CONSTRUCTION = 247
        ROAD = 241
        EMPTY = 233
        num_rows, num_cols = screen.getmaxyx()
        
        #exit()
        path = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [4, 1], [4, 2], [5, 3], [5, 4], [5, 5]]
        for tab in path:
            screen.clear()
            screen.addch(tab[0], tab[1], '■', curses.color_pair(197))
            
            screen.addstr(10, 0, 'Lignes   : ' + str(num_rows))
            screen.addstr(11, 0, 'Colonnes : ' + str(num_cols))
            
            screen.refresh()
            curses.napms(250)

        curses.napms(2000)
        curses.endwin()
    
    def nextTurn(self) -> None:
        pass
    
    # Fusionne les map des S dans self.map
    def updateMap(self) -> None:
        pass