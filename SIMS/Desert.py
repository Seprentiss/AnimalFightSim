import random
from ANIMALS.LARGE.Gorilla import Gorilla
from ANIMALS.LARGE.Grizzly import Grizzly
from ANIMALS.LARGE.Tiger import Tiger
from ANIMALS.LARGE.Elephant import Elephant
from ANIMALS.LARGE.Hippo import Hippo
from ANIMALS.LARGE.Rhino import Rhino
from ANIMALS.LARGE.Lion import Lion
from ANIMALS.LARGE.PolarBear import PolarBear
from ANIMALS.LARGE.Bull import Bull
from ANIMALS.LARGE.Bison import Bison
from ANIMALS.LARGE.Moose import Moose
from ANIMALS.LARGE.Giraffe import Giraffe
from ANIMALS.MEDIUM.Chimpanzee import Chimp
from ANIMALS.MEDIUM.Cougar import Cougar
from ANIMALS.MEDIUM.Jaguar import Jaguar
from ANIMALS.MEDIUM.Wolf import Wolf

from tqdm import trange
import time

global animals, attacks, biteRow, hitRow, currentAnimal, end, currentAnimal, oneCount, twoCount, attacksPerTurn, one, two, num_of_tests


end = False;

currentAnimal = 0

twoCount = 0
oneCount = 0

attacksPerTurn = 0

oneBleeding = False
twoBleeding = False
one = ""
two = ""

num_of_tests = 1000

combatants = []


def AnimalOneSelection(animalOne):
    switcher = {
        "Gorilla": Gorilla(),
        "Grizzly Bear": Grizzly(),
        "Polar Bear": PolarBear(),
        "Tiger": Tiger(),
        "Lion": Lion(),
        "Elephant": Elephant(),
        "Hippo": Hippo(),
        "Rhino": Rhino(),
        "Bull": Bull(),
        "Bison": Bison(),
        "Chimp": Chimp(),
        "Jaguar": Jaguar(),
        "Cougar": Cougar(),
        "Moose": Moose(),
        "Giraffe": Giraffe(),
        "Wolf": Wolf()

    }
    return switcher.get(animalOne, "Invalid Animal")


def AnimalTwoSelection(animalTwo):
    switcher = {
        "Gorilla": Gorilla(),
        "Grizzly Bear": Grizzly(),
        "Polar Bear": PolarBear(),
        "Tiger": Tiger(),
        "Lion": Lion(),
        "Elephant": Elephant(),
        "Hippo": Hippo(),
        "Rhino": Rhino(),
        "Bull": Bull(),
        "Bison": Bison(),
        "Chimp": Chimp(),
        "Jaguar": Jaguar(),
        "Cougar": Cougar(),
        "Moose": Moose(),
        "Giraffe": Giraffe(),
        "Wolf": Wolf()
    }
    return switcher.get(animalTwo, "Invalid Animal")

def Next(current):
    global currentAnimal
    if current == 1:
        currentAnimal = 2
    if current == 2:
        currentAnimal = 1

def RandAnimal(anOne, anTwo):
    aggression_One = anOne.aggression
    aggression_Two = anTwo.aggression

    mean_Aggression = aggression_One + aggression_Two

    aggression_One_Rat = int((aggression_One / mean_Aggression) * 100)
    aggression_Two_Rat = int((aggression_Two / mean_Aggression) * 100)

    if aggression_One_Rat > aggression_Two_Rat:
        num = random.randrange(1, 101)
        if num <= aggression_One_Rat:
            return 1
        if num > 100 - aggression_Two_Rat:
            return 2
    else:
        num = random.randrange(1, 101)
        if num <= aggression_Two_Rat:
            return 2
        if num > 100 - (100 - aggression_One_Rat):
            return 1

def DesertSim(animalOne, animalTwo):
    global biteRow, hitRow, currentAnimal, end, oneCount, twoCount, attacksPerTurn, num_of_tests
    oneCount = 0
    twoCount = 0

    for n in range(num_of_tests):
        end = False
        one = AnimalOneSelection(animalOne)
        two = AnimalTwoSelection(animalTwo)

        one.DesertStatAdj()
        two.DesertStatAdj()

        oneHealth = one.health
        twoHealth = two.health



        currentAnimal = RandAnimal(one, two)

        while ((one.health > 0 or two.health > 0) and end is False):

            if currentAnimal == 2:
                attacksPerTurn = two.attPT
                if one.oppBleed:
                    twoHealth -= two.Bleeding()
                if twoHealth < 0:
                    oneCount += 1
                    end = True
                    break
                if two.oppBleed:
                    oneHealth -= one.Bleeding()
                if oneHealth < 0:
                    twoCount += 1
                    end = True
                    break
                for a in range(int(attacksPerTurn)):
                    attackUsed = two.DesertRandAttack()
                    if one.StrikeEvaded()[0] == "Dodge":
                        oneHealth = oneHealth
                    else:
                        oneHealth -= attackUsed
                    if oneHealth < 0:
                        twoCount += 1
                        attacksPerTurn = 0
                        end = True
                        break
                else:
                    Next(currentAnimal)
            else:
                attacksPerTurn = one.attPT
                if two.oppBleed:
                    oneHealth -= one.Bleeding()
                if oneHealth < 0:
                    twoCount += 1
                    end = True
                    break
                if one.oppBleed:
                    twoHealth -= two.Bleeding()
                if twoHealth < 0:
                    oneCount += 1
                    end = True
                    break
                for b in range(int(attacksPerTurn)):
                    attackUsed = one.DesertRandAttack()
                    if two.StrikeEvaded()[0] == "Dodge":
                        twoHealth = twoHealth
                    else:
                        twoHealth -= attackUsed

                    if twoHealth < 0:
                        oneCount += 1
                        attacksPerTurn = 0
                        end = True
                        break
                else:
                    Next(currentAnimal)

    return (oneCount, twoCount)