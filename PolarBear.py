import pandas as pd
import random

class PolarBear:
    global data,animal, health, speed,bite,punch,slam,attacks,ev,attPT,clawBonus,oppBleed,inTree, oppInTree, attPow
    data = pd.read_csv("animalfight.csv")
    animal = "POLAR BEAR"
    attacks = ["Bite","Claw", "Slam"]
    speed = data.loc[2, animal]
    bite = data.loc[12, animal]
    punch = (data.loc[13,animal])
    slam = punch * 2
    health = data.loc[6,animal]
    ev = data.loc[3, animal]
    attPT = 2
    clawBonus = punch * .1
    oppBleed = False
    inTree = False
    oppInTree = False
    attPow = 0

    def __init__(self):
        global health,speed,bite,punch,slam,attacks,attPT,oppBleed,inTree, opInTree
        self.health = health
        self.speed = speed
        self.attacks = attacks
        self.bite = bite
        self.punch = punch
        self.slam = slam
        self.attPT = attPT
        self.oppBleed = oppBleed
        self.ev = ev
        self.inTree = inTree
        self.oppInTree = oppInTree

    def ClimbTree(self):
        global inTree, attPt
        self.attPT = round(data.loc[14, animal])
        if self.inTree is False and oppInTree is False:
            treeClimbed = random.choices(["Yes", "No"], weights=(0, 100))
            if treeClimbed[0] == "Yes":
                self.inTree = True
                self.attPT -= 1
                return self.inTree
            else:
                return self.inTree
        if self.inTree is False and oppInTree is True:
            treeClimbed = random.choices(["Yes", "No"], weights=(0, 100))
            if treeClimbed[0] == "Yes":
                self.inTree = True
                self.attPT -= 1
                return self.inTree
            else:
                return self.inTree
        else:
            treeClimbed = random.choices(["Yes", "No"], weights=(100, 0))
            if treeClimbed[0] == "Yes":
                self.inTree = False
                self.attPT -= 1
                return self.inTree
            else:
                return self.inTree



    def PlainsRandAttack(self):
        global attacks,clawBonus,bleeding
        att = random.choices(attacks, weights=(55, 25, 25), k=1)
        if att[0] == "Bite":
            hit = random.choices(['T','F'], weights=(7,93))
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.bite
                rB = random.choices(['T','F'], weights=(45,55))
                if rB[0] == "T":
                    self.OppBleed()
        if att[0] == "Claw":
            hit = random.choices(['T', 'F'], weights=(10, 90))
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.punch + clawBonus
                rB = random.choices(['T', 'F'], weights=(20, 80))
                if rB[0] == "T":
                    self.OppBleed()
        if att[0] == "Slam":
            hit = random.choices(['T', 'F'], weights=(10, 90))
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.slam
        return attPow

    def JungleRandAttack(self):
        global attacks, bleeding, inTree, oppInTree, attPow, clawBonus
        if self.inTree is True and oppInTree is False:
            hit = random.choices(['T', 'F'], weights=(30, 70))
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = 0
            return attPow
        if self.inTree is True and oppInTree is True:
            self.attacks = ["Bite", "Claw", "Slam"]
            att = random.choices(attacks, weights=(55, 15, 30), k=1)
            if att[0] == "Bite":
                hit = random.choices(['T', 'F'], weights=(30, 70))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.bite
                    rB = random.choices(['T', 'F'], weights=(40, 60))
                    if rB[0] == "T":
                        self.OppBleed()
            if att[0] == "Claw":
                hit = random.choices(['T', 'F'], weights=(40, 60))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.punch + clawBonus
            if att[0] == "Slam":
                hit = random.choices(['T', 'F'], weights=(80, 20))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = 500
                    oppInTree = False
            return attPow

        if self.inTree is False and oppInTree is True:
            att = random.choices(attacks, weights=(65, 25, 10), k=1)
            if att[0] == "Bite":
                hit = random.choices(['T', 'F'], weights=(100, 0))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.bite
                    rB = random.choices(['T', 'F'], weights=(40, 60))
                    if rB[0] == "T":
                        self.OppBleed()
            if att[0] == "Claw":
                hit = random.choices(['T', 'F'], weights=(100, 0))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.punch + clawBonus
            if att[0] == "Slam":
                hit = random.choices(['T', 'F'], weights=(100, 0))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.slam
            return attPow
        else:
            att = random.choices(attacks, weights=(55, 25, 25), k=1)
            if att[0] == "Bite":
                hit = random.choices(['T', 'F'], weights=(7, 93))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.bite
                    rB = random.choices(['T', 'F'], weights=(45, 55))
                    if rB[0] == "T":
                        self.OppBleed()
            if att[0] == "Claw":
                hit = random.choices(['T', 'F'], weights=(10, 90))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.punch + clawBonus
                    rB = random.choices(['T', 'F'], weights=(20, 80))
                    if rB[0] == "T":
                        self.OppBleed()
            if att[0] == "Slam":
                hit = random.choices(['T', 'F'], weights=(10, 90))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.slam
            return attPow


    def StrikeEvaded(self):
        global ev, data, animal
        dodge = round(ev / 10) + round(data.loc[4, animal] / 10)
        hit = (100 - dodge)

        op = ["Dodge", "Hit"]
        dodged = random.choices(op, weights=(dodge, hit), k=1)
        return dodged
    def Bleeding(self):
        global bleeding, data,animal
        dmg = data.loc[15, animal]
        return dmg


    def OppBleed(self):
        global oppBleed
        oppBleed = True
        self.oppBleed = oppBleed
        return oppBleed

    def JungleStatAdj(self):
        global attacks
        self.ev = self.ev - 10