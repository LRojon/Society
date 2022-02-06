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
        for i in range(0, curses.COLORS):
            curses.init_pair(i + 1, i, -1)
        '''
        COLOR_BLACK =           0
        COLOR_WHITE =           1
        COLOR_FOOD =            2
        COLOR_WATER =           3
        COLOR_SOCIAL =          4
        COLOR_HEALTH =          5
        COLOR_CONSTRUCTION =    6
        COLOR_ROAD =            7
        curses.init_color(COLOR_BLACK       ,   0,      0,      0   )
        curses.init_color(COLOR_WHITE       ,   1000,   1000,   1000)
        curses.init_color(COLOR_FOOD        ,   1000,   500,    0   )
        curses.init_color(COLOR_WATER       ,   0,      0,      1000)
        curses.init_color(COLOR_SOCIAL      ,   976,    894,    717 )
        curses.init_color(COLOR_HEALTH      ,   0,   1000,      1000   )
        curses.init_color(COLOR_CONSTRUCTION,   500,    500,    500 )
        curses.init_color(COLOR_ROAD        ,   250,    250,    250 )
        HUMAN =         1
        FOOD =          2
        WATER =         3
        SOCIAL =        4
        HEALTH =        5
        CONSTRUCTION =  6
        ROAD =          7
        curses.init_pair(HUMAN          , COLOR_BLACK,          COLOR_WHITE)
        curses.init_pair(FOOD           , COLOR_FOOD,           COLOR_BLACK)
        curses.init_pair(WATER          , COLOR_WATER,          COLOR_BLACK)
        curses.init_pair(SOCIAL         , COLOR_SOCIAL,         COLOR_BLACK)
        curses.init_pair(HEALTH         , COLOR_HEALTH,         COLOR_BLACK)
        curses.init_pair(CONSTRUCTION   , COLOR_CONSTRUCTION,   COLOR_BLACK)
        curses.init_pair(ROAD           , COLOR_ROAD,           COLOR_BLACK)
'''
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
        pass
    
    def nextTurn(self) -> None:
        pass
    
    # Fusionne les map des S dans self.map
    def updateMap(self) -> None:
        pass

def main(stdscr):
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)
    try:
        for i in range(0, 255):
            stdscr.addstr(str(i), curses.color_pair(i))
    except curses.ERR:
        # End of screen reached
        pass
    stdscr.getch()

curses.wrapper(main)