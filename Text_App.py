import itertools
import re

import pandas as pd
from tqdm import trange

from SIMS.All_Sims import *


def Start():
    global animals, terrains, combatants, num_of_tests
    animals = pd.read_csv("/Users/spencerprentiss/PycharmProjects/AnimalFightSimulator/animalfight(3).csv").drop(
        columns=['HUMAN', 'CROCODILE'])
    animals.drop(animals.columns[0], axis=1, inplace=True)
    animals = list(animals)
    terrains = ["Plains", "Jungle", "Arctic", "Desert", "All"]
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
        animals = pd.read_csv("/Users/spencerprentiss/PycharmProjects/AnimalFightSimulator/animalfight(3).csv").drop(
            columns=['HUMAN', 'CROCODILE'])
        animals.drop(animals.columns[0], axis=1, inplace=True)
        animals = list(animals)
        e = False
        e2 = False
        tEnd = False
        while not e:
            num_of_tests = 1000
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
                                    output = PlainsSim(anOne.title(), anTwo.title())
                                if terrain == "Jungle":
                                    output = JungleSim(anOne.title(), anTwo.title())
                                if terrain == "Arctic":
                                    output = ArcticSim(anOne.title(), anTwo.title())
                                if terrain == "Desert":
                                    output = (DesertSim(anOne.title(), anTwo.title()))
                                if terrain == "All":
                                    output = (AllSim(anOne.title(), anTwo.title()))
                                if output[0] > output[1]:
                                    if terrain == "All":
                                        num_of_tests = num_of_tests * (len(terrains) - 1)
                                    winP = float(output[0] / (num_of_tests / 100))
                                    print("The " + anOne + " Wins:" + "\nThey Won " + str(
                                        winP) + "% of the Match-ups")
                                if output[1] > output[0]:
                                    if terrain == "All":
                                        num_of_tests = num_of_tests * (len(terrains) - 1)
                                    winP = float(output[1] / (num_of_tests / 100))
                                    print("The " + anTwo + " Wins:" + "\nThey Won " + str(
                                        round(winP, 2)) + "% of the Match-ups")

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


def Tourney():
    animals = pd.read_csv("/Users/spencerprentiss/PycharmProjects/AnimalFightSimulator/animalfight(3).csv").drop(
        columns=['HUMAN', 'CROCODILE'])
    animals.drop(animals.columns[0], axis=1, inplace=True)
    animals = list(animals)

    for a in range(len(animals)):
        animals[a] = animals[a].title()
        animals[a] = animals[a].replace(" ", "")
    combinations = [' '.join(x) for x in itertools.combinations(animals, 2)]

    d = dict()
    for a in animals:
        d[a + " Wins"] = 0

    for combination in trange(len(combinations)):
        if combination == 30:
            print("\nLoading Stats... ")
        if combination == 60:
            print("\nPreparing Battle Field")
        if combination == 90:
            print("\nCalculating Results...")
        a = combinations[combination].split(" ")
        anOne = re.sub(r"(\w)([A-Z])", r"\1 \2", a[0])
        anTwo = re.sub(r"(\w)([A-Z])", r"\1 \2", a[1])

        anOne = anOne.upper()
        anTwo = anTwo.upper()

        output = (AllSim(anOne.title(), anTwo.title()))
        if output[0] > output[1]:
            d[a[0] + " Wins"] += 1
        if output[1] > output[0]:
            d[a[1] + " Wins"] += 1

    print(dict(sorted(d.items(), key=lambda item: item[1], reverse=True)))
