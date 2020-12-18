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

num_of_tests = 10000

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



# Handles all Simulations in the Plains Biome
def PlainsSim(animalOne, animalTwo):
    global biteRow, hitRow, currentAnimal, end, oneCount, twoCount, attacksPerTurn, num_of_tests
    oneCount= 0
    twoCount = 0
    print("Simulating Match-up...\n")
    time.sleep(.5)
    for n in trange(num_of_tests):
        if n == num_of_tests * .25:
            print("\nLoading Stats... ")
        if n == num_of_tests / 2:
            print("\nPreparing Battle Field")
        if n == num_of_tests * .75:
            print("\nCalculating Results...")
        end = False
        one = AnimalOneSelection(animalOne)
        two = AnimalTwoSelection(animalTwo)

        oneHealth = one.health
        twoHealth = two.health

        currentAnimal = random.randrange(1, 3)

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
                    attackUsed = two.PlainsRandAttack()
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
                    attackUsed = one.PlainsRandAttack()
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
