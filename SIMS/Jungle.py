

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

def JungleSim(animalOne, animalTwo):

    global biteRow, hitRow, currentAnimal, end, oneCount, twoCount, attacksPerTurn, num_of_tests
    num_of_tests = 1000
    oneCount = 0
    twoCount = 0

    for n in range(num_of_tests):
        end = False
        one = AnimalOneSelection(animalOne)
        two = AnimalTwoSelection(animalTwo)

        one.JungleStatAdj()
        two.JungleStatAdj()

        oneHealth = one.health
        twoHealth = two.health

        currentAnimal = RandAnimal(one,two)

        while ((one.health > 0 or two.health > 0) and end is False):

            if currentAnimal == 2:
                attacksPerTurn = two.attPT
                if two.isCamouflaged:
                    two.isCamouflaged = False
                    if one.isCamouflaged:
                        spotChance = round(two.intel - (one.size / 10))
                        if spotChance < 0:
                            spotChance = 0
                        spotted = random.choices(["Yes", "No"], weights=(spotChance, 100 - spotChance))
                        if spotted == "Yes":
                            one.isCamouflaged = False
                            one.attPT -= 1
                            if two.CamoAttack() == "hit":
                                attPow = random.choices(['oneHit', 'Norm'], weights=(5, 95))
                                if attPow == "oneHit":
                                    two.attPT -=1
                                    one.health = 0
                                else:
                                    two.attPT -= 1
                                    one.health -= two.JungleRandAttack() * 5
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
                            two.ClimbTree()
                            for a in range(int(attacksPerTurn)):
                                attackUsed = two.JungleRandAttack()
                                if one.StrikeEvaded()[0] == "Dodge":
                                    oneHealth = oneHealth
                                else:
                                    oneHealth -= attackUsed
                                    if one.oppInTree is False:
                                        two.inTree = False
                                if oneHealth < 0:
                                    twoCount += 1
                                    attacksPerTurn = 0
                                    end = True
                                    break
                            else:
                                Next(currentAnimal)
                        else:
                            Next(currentAnimal)
                elif one.isCamouflaged:
                    if one.isCamouflaged:
                        spotChance = round(two.intel - (one.size / 10))
                        if spotChance < 0:
                            spotChance = 0
                        spotted = random.choices(["Yes", "No"], weights=(spotChance, 100 - spotChance))
                        if spotted == "Yes":
                            one.isCamouflaged = False
                            one.attPT -= 1

                            if two.CamoAttack() == "hit":
                                attPow = random.choices(['oneHit', 'Norm'], weights=(5, 95))
                                if attPow == "oneHit":
                                    one.health = 0
                                else:
                                    one.health -= two.JungleRandAttack() * 5
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
                            two.ClimbTree()
                            for a in range(int(attacksPerTurn)):
                                attackUsed = two.JungleRandAttack()
                                if one.StrikeEvaded()[0] == "Dodge":
                                    oneHealth = oneHealth
                                else:
                                    oneHealth -= attackUsed
                                    if one.oppInTree is False:
                                        two.inTree = False
                                if oneHealth < 0:
                                    twoCount += 1
                                    attacksPerTurn = 0
                                    end = True
                                    break
                            else:
                                Next(currentAnimal)
                        else:
                            Next(currentAnimal)
                else:
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
                    two.ClimbTree()
                    for a in range(int(attacksPerTurn)):
                        attackUsed = two.JungleRandAttack()
                        if one.StrikeEvaded()[0] == "Dodge":
                            oneHealth = oneHealth
                        else:
                            oneHealth -= attackUsed
                            if one.oppInTree is False:
                                two.inTree = False
                        if oneHealth < 0:
                            twoCount += 1
                            attacksPerTurn = 0
                            end = True
                            break
                    else:
                        Next(currentAnimal)
            else:
                attacksPerTurn = two.attPT
                if one.isCamouflaged:
                    one.isCamouflaged = False
                    if two.isCamouflaged:
                        spotChance = round((one.intel/10) + (two.size / 50))
                        if spotChance < 0:
                            spotChance = 0
                        spotted = random.choices(["Yes", "No"], weights=(spotChance, 100 - spotChance))
                        if spotted == "Yes":
                            two.isCamouflaged = False
                            two.attPT -= 1
                            if two.CamoAttack() == "hit":
                                attPow = random.choices(['oneHit', 'Norm'], weights=(5, 95))
                                if attPow == "oneHit":
                                    one.attPT -= 1
                                    two.health = 0
                                else:
                                    one.attPT -= 1
                                    two.health -= one.JungleRandAttack() * 5
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
                            one.ClimbTree()
                            for b in range(int(attacksPerTurn)):
                                attackUsed = one.JungleRandAttack()
                                if two.StrikeEvaded()[0] == "Dodge":
                                    twoHealth = twoHealth
                                else:
                                    twoHealth -= attackUsed
                                    if two.oppInTree is False:
                                        one.inTree = False

                                if twoHealth < 0:
                                    oneCount += 1
                                    attacksPerTurn = 0
                                    end = True
                                    break
                            else:
                                Next(currentAnimal)
                        else:
                            Next(currentAnimal)
                elif two.isCamouflaged:
                    spotChance = round((one.intel / 10) + (two.size / 50))
                    if spotChance < 0:
                        spotChance = 0
                    spotted = random.choices(["Yes", "No"], weights=(spotChance, 100 - spotChance))
                    if spotted == "Yes":
                        two.isCamouflaged = False
                        two.attPT -= 1
                        if two.CamoAttack() == "hit":
                            attPow = random.choices(['oneHit', 'Norm'], weights=(5, 95))
                            if attPow == "oneHit":
                                one.attPT -= 1
                                two.health = 0
                            else:
                                one.attPT -= 1
                                two.health -= one.JungleRandAttack() * 5
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
                        one.ClimbTree()
                        for b in range(int(attacksPerTurn)):
                            attackUsed = one.JungleRandAttack()
                            if two.StrikeEvaded()[0] == "Dodge":
                                twoHealth = twoHealth
                            else:
                                twoHealth -= attackUsed
                                if two.oppInTree is False:
                                    one.inTree = False

                            if twoHealth < 0:
                                oneCount += 1
                                attacksPerTurn = 0
                                end = True
                                break
                        else:
                            Next(currentAnimal)
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
                    one.ClimbTree()
                    for b in range(int(attacksPerTurn)):
                        attackUsed = one.JungleRandAttack()
                        if two.StrikeEvaded()[0] == "Dodge":
                            twoHealth = twoHealth
                        else:
                            twoHealth -= attackUsed
                            if two.oppInTree is False:
                                one.inTree = False

                        if twoHealth < 0:
                            oneCount += 1
                            attacksPerTurn = 0
                            end = True
                            break
                    else:
                        Next(currentAnimal)

    return (oneCount, twoCount)
