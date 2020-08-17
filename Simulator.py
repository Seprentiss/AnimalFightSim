import pandas as pd
import numpy as np
import seaborn as sns
import random
from Gorilla import Gorilla
from Grizzly import Grizzly
from Tiger import Tiger
from Elephant import Elephant


global animals, attacks, biteRow, hitRow, currentAnimal, end, currentAnimal, oneCount, twoCount, attacksPerTurn, one, two
data = pd.read_csv("animalfight.csv")


animals = ["Gorilla", "Grizzly Bear", "Polar Bear", "Elephant", "Hippo", "Rhino", "Lion", "Tiger", "Moose", "Crocodile"]

attacks = ["Bite", "Hit", "Slam"]

end = False;

currentAnimal = 0

twoCount = 0
oneCount = 0

attacksPerTurn = 0

oneBleeding = False
twoBleeding = False
one = ""
two = ""

def AnimalOneSelection(animalOne):
    global one
    if animalOne == "Gorilla":
        one = Gorilla()
        return one
    if animalOne == "Grizzly Bear":
        one = Grizzly()
        return one
    if animalOne == "Tiger":
        one = Tiger()
        return one
    if animalOne == "Elephant":
        one = Elephant()
        return one

def AnimalOneSelection(animalTwo):
    global two
    if animalTwo == "Gorilla":
        one = Gorilla()
        return one
    if animalTwo  == "Grizzly Bear":
        one = Grizzly()
        return one
    if animalTwo  == "Tiger":
        one = Tiger()
        return one
    if animalTwo  == "Elephant":
        one = Elephant()
        return one

def Next(current):
    global currentAnimal
    if current == 1:
        currentAnimal = 2
    if current == 2:
        currentAnimal = 1





def Sim(animalOne, animalTwo):
    global biteRow, hitRow, currentAnimal, end, oneCount, twoCount,attacksPerTurn
    num_of_tests = 1000
    for i in range(num_of_tests):
        end = False
        one = AnimalOneSelection(animalOne)
        two = Gorilla()

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
                for a in range(attacksPerTurn):
                    attackUsed = two.RandAttack()
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
                for b in range(attacksPerTurn):
                    attackUsed = one.RandAttack()
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


    print("Wins for " + animalOne + " " + str(oneCount))
    print("Wins for " + animalTwo + " " + str(twoCount))
def Start():
    global animals
    combatants = animals
    print(*combatants, sep="\n")
    anOne = input("Please Select Your First Combatant")

Start()
