import sys, time, pygame

def makeRoad(x : int, y : int):
    top = False
    bottom = False
    left = False
    right = False
    if x > 0:
        left = map_society[x - 1][y] == "R"
    if x < len(map_society[0]):
        right = map_society[x + 1][y] == "R"
    if y > 0:
        top = map_society[x][y - 1] == "R"
    if y < len(map_society):
        bottom = map_society[x][y + 1] == "R"
        
    char = str(int(top)) + str(int(bottom)) + str(int(left)) + str(int(right))
    
    if char == '0000' or char == '0100' or char == '1000' or char == '1100':
        return 0
    elif char == '0001' or char == '0010' or char == '0011':
        return 1
    elif char == '1111':
        return 2
    elif char == '1101':
        return 3
    elif char == '0111':
        return 4
    elif char == '1110':
        return 5
    elif char == '1011':
        return 6
    elif char == '0101':
        return 7
    elif char == '0110':
        return 8
    elif char == '1010':
        return 9
    elif char == '1001':
        return 10

map_society = [
    ["V", "V", "V", "V", "V", "V", "V"],
    ["V", "V", "R", "F", "R", "V", "V"],
    ["V", "R", "R", "R", "R", "R", "V"],
    ["V", "H", "R", "S", "R", "W", "V"],
    ["V", "R", "R", "R", "R", "R", "V"],
    ["V", "V", "R", "C", "R", "V", "V"],
    ["V", "V", "V", "V", "V", "V", "V"],
]

pygame.init()

size = width, height = 224, 224
tileSize = 32
background = 249, 228, 183

screen = pygame.display.set_mode(size)

ROAD = [pygame.image.load('Assets/Road/Road' + str(i) + '.png').convert() for i in range(1, 12)]
ROAD_RECT = [ROAD[i].get_rect() for i in range(0, 11)]

FOOD = pygame.image.load('Assets/Food.png')
FOOD_RECT = FOOD.get_rect()
WATER = pygame.image.load('Assets/Water.png')
WATER_RECT = WATER.get_rect()
HEALTH = pygame.image.load('Assets/Health.png')
HEALTH_RECT = HEALTH.get_rect()
SOCIAL = pygame.image.load('Assets/Social.png')
SOCIAL_RECT = SOCIAL.get_rect()
CONSTRUCTION = pygame.image.load('Assets/Construction.png')
CONSTRUCTION_RECT = CONSTRUCTION.get_rect()

PATTERN = pygame.image.load('Assets/pattern.png')

screen.fill(background)
for x in range(0, len(map_society)):
    for y in range(0, len(map_society[0])):
        if PATTERN.get_at((x, y)) == pygame.Color(255, 127, 0):
            FOOD_RECT.x = x * tileSize
            FOOD_RECT.y = y * tileSize
            screen.blit(FOOD, FOOD_RECT)
        elif PATTERN.get_at((x, y)) == pygame.Color(0, 0, 255):
            WATER_RECT.x = x * tileSize
            WATER_RECT.y = y * tileSize
            screen.blit(WATER, WATER_RECT)
        elif PATTERN.get_at((x, y)) == pygame.Color(127, 127, 127):
            CONSTRUCTION_RECT.x = x * tileSize
            CONSTRUCTION_RECT.y = y * tileSize
            screen.blit(CONSTRUCTION, CONSTRUCTION_RECT)
        elif PATTERN.get_at((x, y)) == pygame.Color(255, 0, 0):
            HEALTH_RECT.x = x * tileSize
            HEALTH_RECT.y = y * tileSize
            screen.blit(HEALTH, HEALTH_RECT)
        elif PATTERN.get_at((x, y)) == pygame.Color(255, 0, 255):
            SOCIAL_RECT.x = x * tileSize
            SOCIAL_RECT.y = y * tileSize
            screen.blit(SOCIAL, SOCIAL_RECT)
        elif PATTERN.get_at((x, y)) == pygame.Color(255, 255, 255):
            idRoad = makeRoad(x, y)
            ROAD_RECT[idRoad].x = x * tileSize
            ROAD_RECT[idRoad].y = y * tileSize
            screen.blit(ROAD[idRoad], ROAD_RECT[idRoad])

pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
