import pandas as pd
import random

class Tiger:
    global data,animal, health, speed,bite,punch,slam,attacks,ev,attPT,clawBonus,oppBleed,inTree, oppInTree, attPow
    data = pd.read_csv("animalfight.csv")
    animal = "TIGER"
    attacks = ["Bite","Claw"]
    speed = data.loc[2, animal]
    bite = data.loc[12, animal]
    punch = data.loc[13, animal]
    health = data.loc[6,animal]
    ev = data.loc[3, animal]
    attPT = round(data.loc[14, animal])
    clawBonus = punch * .3
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
        self.attPT = attPT
        self.oppBleed = oppBleed
        self.ev = ev
        self.inTree = inTree
        self.oppInTree = oppInTree

    def ClimbTree(self):
        global inTree, attPt
        self.attPT = round(data.loc[14, animal])
        if self.inTree is False and oppInTree is False:
            treeClimbed = random.choices(["Yes", "No"], weights=(5, 95))
            if treeClimbed[0] == "Yes":
                self.inTree = True
                self.attPT -= 1
                return self.inTree
            else:
                return self.inTree
        if self.inTree is False and oppInTree is True:
            treeClimbed = random.choices(["Yes", "No"], weights=(60, 40))
            if treeClimbed[0] == "Yes":
                self.inTree = True
                self.attPT -= 1
                return self.inTree
            else:
                return self.inTree
        else:
            treeClimbed = random.choices(["Yes", "No"], weights=(70, 30))
            if treeClimbed[0] == "Yes":
                self.inTree = False
                self.attPT -= 1
                return self.inTree
            else:
                return self.inTree




    def PlainsRandAttack(self):
        global attacks, clawBonus, bleeding, attPow
        att = random.choices(attacks, weights=(40, 60), k=1)
        if att[0] == "Bite":
            hit = random.choices(['T', 'F'], weights=(5, 95))
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.bite
                rB = random.choices(['T', 'F'], weights=(50, 50))
                if rB[0] == "T":
                    self.OppBleed()
        if att[0] == "Claw":
            hit = random.choices(['T', 'F'], weights=(5, 95))
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.punch + clawBonus
                rB = random.choices(['T', 'F'], weights=(65, 35))
                if rB[0] == "T":
                    self.OppBleed()
        return attPow


    def JungleRandAttack(self):
        global attacks, bleeding, inTree, oppInTree, attPow
        if self.inTree is True and oppInTree is False:
            hit = random.choices(['T', 'F'], weights=(40, 60))
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = 0
            return attPow
        if self.inTree is True and oppInTree is True:
            self.attacks = ["Bite", "Claw"]
            att = random.choices(attacks, weights=(40, 60), k=1)
            if att[0] == "Bite":
                hit = random.choices(['T', 'F'], weights=(10, 90))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.bite
                    rB = random.choices(['T', 'F'], weights=(60, 40))
                    if rB[0] == "T":
                        self.OppBleed()
            if att[0] == "Claw":
                hit = random.choices(['T', 'F'], weights=(10, 80))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.punch + clawBonus
                    rB = random.choices(['T', 'F'], weights=(70, 30))
                    if rB[0] == "T":
                        self.OppBleed()
            return attPow

        if self.inTree is False and self.oppInTree is True:
            att = random.choices(attacks, weights=(40,60), k=1)
            if att[0] == "Bite":
                hit = random.choices(['T', 'F'], weights=(100, 0))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.bite
                    rB = random.choices(['T', 'F'], weights=(50, 50))
                    if rB[0] == "T":
                        self.OppBleed()
            if att[0] == "Claw":
                hit = random.choices(['T', 'F'], weights=(100, 0))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.punch
            return attPow
        else:
            att = random.choices(attacks, weights=(40, 60), k=1)
            if att[0] == "Bite":
                hit = random.choices(['T', 'F'], weights=(5, 95))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.bite
                    rB = random.choices(['T', 'F'], weights=(50, 50))
                    if rB[0] == "T":
                        self.OppBleed()
            if att[0] == "Claw":
                hit = random.choices(['T', 'F'], weights=(5, 95))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.punch + clawBonus
                    rB = random.choices(['T', 'F'], weights=(65, 35))
                    if rB[0] == "T":
                        self.OppBleed()
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
        self.ev = self.ev + 150
