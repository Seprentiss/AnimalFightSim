import random
from Gorilla import Gorilla
from Grizzly import Grizzly
from Tiger import Tiger
from Elephant import Elephant
from Hippo import Hippo
from Rhino import Rhino
from Lion import Lion
from PolarBear import PolarBear
from Bull import Bull
from Bison import Bison
from tqdm import trange
import time

global animals, attacks, biteRow, hitRow, currentAnimal, end, currentAnimal, oneCount, twoCount, attacksPerTurn, one, two, num_of_tests

animals = ["Gorilla", "Grizzly Bear", "Polar Bear", "Elephant", "Hippo", "Rhino", "Lion", "Tiger", "Bull", "Bison"]
terrains =["Plains", "Jungle", "Arctic","Desert"]

end = False;

currentAnimal = 0

twoCount = 0
oneCount = 0

attacksPerTurn = 0

oneBleeding = False
twoBleeding = False
one = ""
two = ""

num_of_tests = 100000

combatants = []


def AnimalOneSelection(animalOne):
    switcher = {
        "Gorilla": Gorilla(),
        "Grizzly Bear": Grizzly(),
        "Polar Bear": PolarBear()  ,
        "Tiger": Tiger(),
        "Lion": Lion(),
        "Elephant": Elephant(),
        "Hippo": Hippo(),
        "Rhino": Rhino(),
        "Bull": Bull(),
        "Bison": Bison()
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
        "Bison": Bison()
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
    oneCount=0
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

    if oneCount > twoCount:
        winP = float(oneCount / (num_of_tests / 100))
        print("The " + animalOne + " Wins:" + "\nThey Won " + str(winP) + "% of the Match-ups")
    if twoCount > oneCount:
        winP = float(twoCount / (num_of_tests / 100))
        print("The " + animalTwo + " Wins:" + "\nThey Won " + str(winP) + "% of the Match-ups")



# Handles all Simulations in the Jungle Biome
def JungleSim(animalOne, animalTwo):
    global biteRow, hitRow, currentAnimal, end, oneCount, twoCount, attacksPerTurn, num_of_tests
    oneCount = 0
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

        one.JungleStatAdj()
        two.JungleStatAdj()

        oneHealth = one.health
        twoHealth = two.health

        currentAnimal = random.randrange(1, 3)

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
    if oneCount > twoCount:
        winP = float(oneCount / (num_of_tests / 100))
        print("The " + animalOne + " Wins:" + "\nThey Won " + str(winP) + "% of the Match-ups")
    if twoCount > oneCount:
        winP = float(twoCount / (num_of_tests / 100))
        print("The " + animalTwo + " Wins:" + "\nThey Won " + str(winP) + "% of the Match-ups")


def ArcticSim(animalOne, animalTwo):
    global biteRow, hitRow, currentAnimal, end, oneCount, twoCount, attacksPerTurn, num_of_tests
    oneCount = 0
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

        one.ArcticStatAdj()
        two.ArcticStatAdj()

        oneHealth = one.health
        twoHealth = two.health

        currentAnimal = random.randrange(1, 3)

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
                                    one.health -= two.ArcticRandAttack() * 5
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
                                attackUsed = two.ArcticRandAttack()
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
                                    one.health -= two.ArcticRandAttack() * 5
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
                                attackUsed = two.ArcticRandAttack()
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
                    for a in range(int(attacksPerTurn)):
                        attackUsed = two.ArcticRandAttack()
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

                            for b in range(int(attacksPerTurn)):
                                attackUsed = one.ArcticRandAttack()
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
                                two.health -= one.ArcticRandAttack() * 5
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
                            attackUsed = one.ArcticRandAttack()
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
                        attackUsed = one.ArcticRandAttack()
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
    if oneCount > twoCount:
        winP = float(oneCount / (num_of_tests / 100))
        print("The " + animalOne + " Wins:" + "\nThey Won " + str(winP) + "% of the Match-ups")
    if twoCount > oneCount:
        winP = float(twoCount / (num_of_tests / 100))
        print("The " + animalTwo + " Wins:" + "\nThey Won " + str(winP) + "% of the Match-ups")


# Handles all Simulations in the Plains Biome
def DesertSim(animalOne, animalTwo):
    global biteRow, hitRow, currentAnimal, end, oneCount, twoCount, attacksPerTurn, num_of_tests
    oneCount = 0
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

        one.DesertStatAdj()
        two.DesertStatAdj()

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


    if oneCount > twoCount:
        winP = float(oneCount / (num_of_tests / 100))
        print("The " + animalOne + " Wins:" + "\nThey Won " + str(winP) + "% of the Match-ups")
    if twoCount > oneCount:
        winP = float(twoCount / (num_of_tests / 100))
        print("The " + animalTwo + " Wins:" + "\nThey Won " + str(winP) + "% of the Match-ups")







# Handles Start up and Selection of animals and terrain
def Start():
    global animals, terrains, combatants
    combatants = animals
    e = False
    e2 = False

    tEnd = False

    contSim = False

    print("=====================\n"
          "Welcome to the Animal Fight Simulator\n"
          "The Purpose of this program is to settle the debate of what animal would win in a fight\n"
          "=====================\n")

    cont = input("Would you like to use the Animal Fight Simulator? Type 0 for No and 1 for Yes: ")
    if cont == "1":
        contSim = True
    while contSim:
        animals = ["Gorilla", "Grizzly Bear", "Polar Bear", "Elephant", "Hippo", "Rhino", "Lion", "Tiger", "Bull",
                   "Bison"]
        e = False
        e2 = False
        tEnd = False
        while not e:
            print("")
            print(*combatants, sep="\n")
            anOne = input("Please Select Your First Combatant From The List Above: ")
            if anOne in animals:
                index = anOne
                remCombatants = animals
                remCombatants.remove(index)

                e = True
                while not e2:
                    print("")
                    print(*remCombatants, sep="\n")
                    anTwo = input("\nPlease Select Your Second Combatant From The List OF Remaining Animals Above: ")
                    if anTwo in remCombatants:
                        index = anTwo
                        remCombatants.remove(index)
                        e2 = True
                        time.sleep(.7)

                        while not tEnd:
                            print("")
                            print(*terrains, sep="\n")
                            terrain = input("Please Select The Terrain: ")
                            if terrain in terrains:
                                tEnd = True
                                if terrain == "Plains":
                                    PlainsSim(anOne, anTwo)
                                if terrain == "Jungle":
                                    JungleSim(anOne, anTwo)
                                if terrain == "Arctic":
                                    ArcticSim(anOne, anTwo)
                                if terrain == "Desert":
                                    DesertSim(anOne, anTwo)
                            else:
                                print("\nTerrain Not Available\nTry Again\n")
                    else:
                        print("\nAnimal Not Found\nTry Again\n")
            else:
                print("Try again")
        cont = input("\nWould you like to run another sim? Type 0 to quit and 1 to continue ")
        if cont == "1":
            contSim = True
        else:
            print("Thank you for using the Animal Fight Simulator")
            SystemExit
            break



Start()
