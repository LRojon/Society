'''
from Entity.society import Society

s = Society("Test")
s.genMap(3,3)
s.printMap()
s.printHumans()
'''
# ╬╩╦╣╠╝╚╗╔║═
import curses
from operator import le
from turtle import right

map_society = [
    ["V", "V", "V", "V", "V", "V", "V"],
    ["V", "V", "R", "F", "R", "V", "V"],
    ["V", "R", "R", "R", "R", "R", "V"],
    ["V", "H", "R", "S", "R", "W", "V"],
    ["V", "R", "R", "R", "R", "R", "V"],
    ["V", "V", "R", "C", "R", "V", "V"],
    ["V", "V", "V", "V", "V", "V", "V"]
]

def makeRoad(x : int, y : int):
    top = False
    bottom = False
    left = False
    right = False
    if y > 0:
        left = map_society[y - 1][x] == "R"
    if y < len(map_society[0]):
        right = map_society[y + 1][x] == "R"
    if x > 0:
        top = map_society[y][x - 1] == "R"
    if x < len(map_society):
        bottom = map_society[y][x + 1] == "R"
    char = str(int(top)) + str(int(bottom)) + str(int(left)) + str(int(right))
    
    if char == '0000' or char == '0100' or char == '1000' or char == '1100':
        return '║'
    elif char == '0001' or char == '0010' or char == '0011':
        return '═'
    elif char == '0101':
        return '╔'
    elif char == '0110':
        return '╗'
    elif char == '0111':
        return '╦'
    elif char == '1001':
        return '╚'
    elif char == '1010':
        return '╝'
    elif char == '1011':
        return '╩'
    elif char == '1101':
        return '╠'
    elif char == '1110':
        return '╣'
    elif char == '1111':
        return '╬'

def printWorld(screen) -> None:
    screen = curses.initscr()
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()

    curses.init_pair(1  , curses.COLOR_BLACK,   curses.COLOR_WHITE)
    for i in range(1, 255):
        curses.init_pair(i + 1, i, -1)
    HUMAN = curses.color_pair(0)
    SELECTED_HUMAN = curses.color_pair(1)
    FOOD = curses.color_pair(95)
    WATER = curses.color_pair(10)
    SOCIAL = curses.color_pair(211)
    HEALTH = curses.color_pair(197)
    CONSTRUCTION = curses.color_pair(247)
    ROAD = curses.color_pair(241)
    EMPTY = curses.color_pair(233)
    
    for x in range(0, len(map_society)):
        for y in range(0, len(map_society[0])):
            if map_society[x][y] == 'V':
                screen.addch(x, y, ' ', EMPTY)
            elif map_society[x][y] == "R":
                screen.addch(x, y, makeRoad(x, y), ROAD)
            elif map_society[x][y] == "F":
                screen.addch(x, y, '♣', FOOD)
            elif map_society[x][y] == "W":
                screen.addch(x, y, '¤', WATER)
            elif map_society[x][y] == "S":
                screen.addch(x, y, '♦', SOCIAL)
            elif map_society[x][y] == "H":
                screen.addch(x, y, '♥', HEALTH)
            elif map_society[x][y] == "C":
                screen.addch(x, y, '⌂', CONSTRUCTION)

    screen.getch()

curses.wrapper(printWorld)