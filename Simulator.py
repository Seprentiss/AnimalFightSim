
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


animals = ["Gorilla", "Grizzly Bear", "Polar Bear", "Elephant", "Hippo", "Rhino", "Lion", "Tiger","Bull","Bison"]

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


def AnimalOneSelection(animalOne):
    global one
    if animalOne == "Gorilla":
        one = Gorilla()
        return one
    if animalOne == "Grizzly Bear":
        one = Grizzly()
        return one
    if animalOne == "Polar Bear":
        one = PolarBear()
        return one
    if animalOne == "Tiger":
        one = Tiger()
        return one
    if animalOne == "Lion":
        one = Lion()
        return one
    if animalOne == "Elephant":
        one = Elephant()
        return one
    if animalOne == "Hippo":
        one = Hippo()
        return one
    if animalOne == "Rhino":
        one = Rhino()
        return one
    if animalOne == "Bull":
        one = Bull()
        return one
    if animalOne == "Bison":
        one = Bison()
        return one


def AnimalTwoSelection(animalTwo):
    global two
    if animalTwo == "Gorilla":
        two = Gorilla()
        return two
    if animalTwo == "Grizzly Bear":
        two = Grizzly()
        return two
    if animalTwo == "Polar Bear":
        two = PolarBear()
        return two
    if animalTwo == "Tiger":
        two = Tiger()
        return two
    if animalTwo == "Lion":
        two = Lion()
        return two
    if animalTwo == "Elephant":
        two = Elephant()
        return two
    if animalTwo == "Hippo":
        two = Hippo()
        return two
    if animalTwo == "Rhino":
        two = Rhino()
        return two
    if animalTwo == "Bull":
        two = Bull()
        return two
    if animalTwo == "Bison":
        two = Bison()
        return two


def Next(current):
    global currentAnimal
    if current == 1:
        currentAnimal = 2
    if current == 2:
        currentAnimal = 1


def PlainsSim(animalOne, animalTwo):
    global biteRow, hitRow, currentAnimal, end, oneCount, twoCount, attacksPerTurn,num_of_tests
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

def JungleSim(animalOne, animalTwo):
    global biteRow, hitRow, currentAnimal, end, oneCount, twoCount, attacksPerTurn, num_of_tests
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
                two.ClimbTree()
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
                attacksPerTurn = one.attPT
                one.ClimbTree()
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

def Start():
    global animals
    combatants = animals
    e = False
    e2 = False

    print("=====================\n"
          "Welcome to the Animal Fight Simulator\n"
          "The Purpose of this program is to settle the debate of what animal would win in a fight\n"
          "=====================")

    while not e:
        print(*combatants, sep="\n")
        anOne = input("Please Select Your First Combatant: ")
        if anOne in combatants:
            index = anOne
            combatants.remove(index)
            e = True
            while not e2:
                print(*combatants, sep="\n")
                anTwo = input("Please Select Your Second Combatant: ")
                if anTwo in combatants:
                    index = anTwo
                    combatants.remove(index)
                    e2 = True
                    time.sleep(.7)
                    JungleSim(anOne, anTwo)
                else:
                    print("\nAnimal Not Found\nTry Again\n")
        else:
            print("Try again")


Start()