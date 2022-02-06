# Sommaire
- [Idée de base](#idée-de-base)
- [Brainstorm](#brainstorm)
  - [Deux types de construction:](#deux-types-de-construction)
  - [Habitant :](#habitant-)
- [Génération](#génération)
- [Objet](#objet)
  - [Utils](#utils)
  - [World](#world)
    - [Construction](#construction)
  - [Society](#society)
    - [Human](#human)
# Idée de base
Générateur et simulateur de société, où l'on pourras voir évoluer chaque personne ainsi que la/les société.s existant dans ce monde.

# Brainstorm
## Deux types de construction:
- Bâtiment : Ils répondent à un besoins ou servent d'habitations
- Route : Servent à se déplacer
- Les H peuvent construire de nouvelles construction grâce au bâtiment de construction (fourni des "graines" de bâtiment)
- Chaque construction aura une capacité d'acceuil maximum prédéfini

## Habitant : 
- Ils possedent des barre de besoins, plus ou moins grande, qui diminue avec le temps
- Quand une de ces barres atteint 0 l'H meurt
- Ils peuvent construire des B/R
- Ils devront rentrer dans les B pour remplire leur besoins
- Les H ne peuvent pas se superposer

# Génération
Society (name: str, nbHInit : int)  
&nbsp;&nbsp;|  
&nbsp;&nbsp;└-> Human ()  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└-> Needs (type)  
&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;Needs (type, max, threslhold)  
  
World (width, height, societies)  
&nbsp;&nbsp;|  
&nbsp;&nbsp;└-> Society.genMap (width, height, originX, origin Y)

# Objet
## Utils
```Python
class Point:
    def __init__(x : int = -1, y : int = -1) -> None:
```
```Python
def rand(max : int, min : int = 0) -> int:
    # Renvoie un entier aléatoire entre max et min inclues
```
```Python
def randDice(formula : str) -> int:
    # Renvoie un entier aléatoire soumis à la formule <formula>
    # <formula> doit être sous la forme <x>d<y>[+<z>] où x, y, z sont des entiers
```
```python
def generateName(nb : int = 3) -> str:
    # Renvoie un nom généré aléatoirement de <nb> syllabes
```
## World
```python
class World:
    def __init__(width : int, height : int, societies : List[Society]) -> None:
    def isInSociety(x : int, y : int) -> bool:
        # Vérifier que le point donné ne se situe pas dans une société déjà existante
    def printWorld() -> None:
        # Affiche sur la console la carte du monde est toutes informations utile
    def nextTurn() -> None:
        # Gère le passage de tour (unité temporelle)
    def updateMap() -> None:
        # Fusionne les map des S dans self.map
```
## Construction
```python
class TypeConstruction:
    def __init__(type : str) -> None:
        # Les valeurs de <type> sont : Food, Water, Social, Health, Construction, et Road
```
```python
class Construction:
    def __init__(type : str, x : int, y : int, cost : Dict[str, int]) -> None:
        # Les valeurs de <type> sont : Food, Water, Social, Health, Construction, et Road
    def use() -> Dict[str, int]:
        # Renvoie un dictionaire de besoins, avec la valeur à ajouter
    def isFull() -> bool: # Anciennement getCapacity
        # Renvoie True si la C est pleine, sinon renvoie False
    def toString() -> str:
        # Renvoie la convertion de la C en string
```
## Society
```python
class Society:
    def __init__(name : str = "", nbHInit : int = 5) -> None:
    def genMap(originX : int, originY : int, width : int = 7, height : int = 7) -> None:
        # Génère la carte de connaissance de la S et place les H au bâtiment social
    def updateMap() -> None:
        # Met à jour la carte de connaissance de la S
    def nextTurn() -> None:
        # Gère le passage de tour (unité temporelle)
    def printHumans() -> None: # ! Déprécié !
        # Affiche le nom de tous les H de la S
```
## Human
```python
class Need:
    def __init__(name : str, nbMax : int = 100, threshold : int = 25) -> None:
    def getNb() -> int:
        # Obtient le nombre actuel du besoin
    def setNb(value : int) -> None:
        # Modifie le nombre actuel du besoin
    def downNeed() -> None:
        # Diminue le nombre actuel du besoin de 1
```
```python
class Human:
    def __init__(parents : List[Human] = []) -> None:
    def generateName() -> str:
        # Génère un nom aléatoirement et suivant l'héritage
    def generateNeeds(list_Needs : List[str]) -> List[Need]:
        # Génère la liste des besoins de l'H
    def nextTurn() -> bool:
        # Gère le passage du tour (unité temporelle) et renvoie l'état de l'H, False = Vivant, True = Mort 
    def makeCracCracBoomBoom() -> None:
        # Dépendamment de l'aléatoire, insert H dans S
    def interact() -> None:
        # Interagit avec World au coordonnées de l'H
    def getPathfinding(x : int, y : int) -> Point:
        # Renvoie les coordonnées du prochain déplacement
```