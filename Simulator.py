import pandas as pd
import numpy as np
import seaborn as sns
import random
from Gorilla import Gorilla
from Grizzly import Grizzly


global animals, attacks, biteRow, hitRow, currentAnimal, end, currentAnimal, oneCount, twoCount, attacksPerTurn
data = pd.read_csv("animalfight.csv")

biteRow = 11
hitRow = 12

animals = ["Gorilla", "Grizzly Bear", "Polar Bear", "Elephant", "Hippo", "Rhino", "Lion", "Tiger", "Moose", "Crocodile"]

attacks = ["Bite", "Hit", "Slam"]

end = False;

currentAnimal = 0

twoCount = 0
oneCount = 0

attacksPerTurn = 0

oneBleeding = False
twoBleeding = False


def Next(current):
    global currentAnimal
    if current == 1:
        currentAnimal = 2
    if current == 2:
        currentAnimal = 1



def Start():
    Sim("Gorilla", "Grizzly Bear")


def Sim(animalOne, animalTwo):
    global biteRow, hitRow, currentAnimal, end, oneCount, twoCount,attacksPerTurn
    num_of_tests = 10000
    for i in range(num_of_tests):
        end = False
        one = Gorilla()
        two = Grizzly()

        oneHealth = one.health
        twoHealth = two.health


        currentAnimal = random.randrange(1, 3)


        while ((oneHealth > 0 or twoHealth > 0) and end is False):

            if currentAnimal == 2:

                attacksPerTurn = two.attPT
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
                for b in range(attacksPerTurn):
                    attackUsed = one.RandAttack()
                    if two.StrikeEvaded()[0] == "Dodge":
                        twoHealth = twoHealth
                        attacksPerTurn -= 1
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

Start()
