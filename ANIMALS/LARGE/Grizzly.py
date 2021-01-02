import math

import pandas as pd
import random


class Grizzly:
    global grizz_data, animal, health, speed, bite, punch, slam, attacks, ev, attPT, clawBonus, oppBleed, inTree, oppInTree, attPow, size, intel,isCamouflaged
    grizz_data = pd.read_csv("/Users/spencerprentiss/PycharmProjects/AnimalFightSimulator/animalfight(3).csv")
    animal = "GRIZZLY BEAR"
    attacks = ["Bite", "Claw", "Slam"]
    speed = grizz_data.loc[2, animal]
    intel = grizz_data.loc[5, animal]
    size = grizz_data.loc[9, animal]
    bite = grizz_data.loc[12, animal]
    punch = (grizz_data.loc[13, animal])
    slam = punch * 1.5
    health = grizz_data.loc[6, animal]
    ev = grizz_data.loc[3, animal]
    attPT = round(grizz_data.loc[14, animal])
    clawBonus = punch * .1
    oppBleed = False
    inTree = False
    oppInTree = False
    attPow = 0
    isCamouflaged = False

    def __init__(self):
        global health, speed, bite, punch, slam, attacks, attPT, oppBleed, inTree, opInTree,isCamouflaged, aggression
        self.health = health
        self.speed = speed
        self.size = size
        self.intel = intel
        self.attacks = attacks
        self.bite = bite
        self.punch = punch
        self.slam = slam
        self.attPT = attPT
        self.oppBleed = oppBleed
        self.ev = ev
        self.inTree = inTree
        self.oppInTree = oppInTree
        self.isCamouflaged = isCamouflaged
        self.aggression = grizz_data.loc[16, animal]

    def ClimbTree(self):
        global inTree, attPt
        self.attPT = round(grizz_data.loc[14, animal])
        if self.inTree is False and oppInTree is False:
            treeClimbed = random.choices(["Yes", "No"], weights=(10, 90))
            if treeClimbed[0] == "Yes":
                self.inTree = True
                self.attPT -= 1
                return self.inTree
            else:
                return self.inTree
        if self.inTree is False and oppInTree is True:
            treeClimbed = random.choices(["Yes", "No"], weights=(30, 70))
            if treeClimbed[0] == "Yes":
                self.inTree = True
                self.attPT -= 1
                return self.inTree
            else:
                return self.inTree
        else:
            treeClimbed = random.choices(["Yes", "No"], weights=(30, 70))
            if treeClimbed[0] == "Yes":
                self.inTree = False
                self.attPT -= 1
                return self.inTree
            else:
                return self.inTree

    def CamoAttack(self):
        global attacks, clawBonus, bleeding, attPow
        hit = random.choices(['T', 'F'], weights=(95, 5))
        if hit[0] == "T":
            return "hit"
        else:
            return "miss"

    def PlainsRandAttack(self):
        global attacks, clawBonus, bleeding
        att = random.choices(attacks, weights=(60, 35, 5), k=1)
        if att[0] == "Bite":
            hit = random.choices(['T', 'F'], weights=(5, 100))
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.bite
                rB = random.choices(['T', 'F'], weights=(40, 60))
                if rB[0] == "T":
                    self.OppBleed()
        if att[0] == "Claw":
            hit = random.choices(['T', 'F'], weights=(10, 90))
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.punch + clawBonus
                rB = random.choices(['T', 'F'], weights=(50, 50))
                if rB[0] == "T":
                    self.OppBleed()
        if att[0] == "Slam":
            hit = random.choices(['T', 'F'], weights=(10, 95))
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.slam
        return attPow

    def JungleRandAttack(self):
        global attacks, bleeding, inTree, oppInTree, attPow,clawBonus
        if self.inTree is True and oppInTree is False:
            hit = random.choices(['T', 'F'], weights=(30, 70))
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = 0
            return attPow
        if self.inTree is True and oppInTree is True:
            self.attacks = ["Bite", "Claw", "Tree Throw"]
            att = random.choices(attacks, weights=(55, 15, 30), k=1)
            if att[0] == "Bite":
                hit = random.choices(['T', 'F'], weights=(30,70))
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
            if att[0] == "Tree Throw":
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
            att = random.choices(attacks, weights=(60, 35, 5), k=1)
            if att[0] == "Bite":
                hit = random.choices(['T', 'F'], weights=(5, 100))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.bite
                    rB = random.choices(['T', 'F'], weights=(40, 60))
                    if rB[0] == "T":
                        self.OppBleed()
            if att[0] == "Claw":
                hit = random.choices(['T', 'F'], weights=(10, 90))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.punch + clawBonus
                    rB = random.choices(['T', 'F'], weights=(50, 50))
                    if rB[0] == "T":
                        self.OppBleed()
            if att[0] == "Slam":
                hit = random.choices(['T', 'F'], weights=(10, 95))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.slam
            return attPow

    def ArcticRandAttack(self):
        global attacks, clawBonus, bleeding
        att = random.choices(attacks, weights=(60, 35, 5), k=1)
        if att[0] == "Bite":
            hit = random.choices(['T', 'F'], weights=(5, 100))
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.bite
                rB = random.choices(['T', 'F'], weights=(40, 60))
                if rB[0] == "T":
                    self.OppBleed()
        if att[0] == "Claw":
            hit = random.choices(['T', 'F'], weights=(10, 90))
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.punch + clawBonus
                rB = random.choices(['T', 'F'], weights=(50, 50))
                if rB[0] == "T":
                    self.OppBleed()
        if att[0] == "Slam":
            hit = random.choices(['T', 'F'], weights=(10, 95))
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.slam
        return attPow

    def DesertRandAttack(self):
        global attacks, clawBonus, bleeding
        att = random.choices(attacks, weights=(60, 35, 5), k=1)
        if att[0] == "Bite":
            hit = random.choices(['T', 'F'], weights=(5, 100))
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.bite
                rB = random.choices(['T', 'F'], weights=(40, 60))
                if rB[0] == "T":
                    self.OppBleed()
        if att[0] == "Claw":
            hit = random.choices(['T', 'F'], weights=(10, 90))
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.punch + clawBonus
                rB = random.choices(['T', 'F'], weights=(50, 50))
                if rB[0] == "T":
                    self.OppBleed()
        if att[0] == "Slam":
            hit = random.choices(['T', 'F'], weights=(10, 95))
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.slam
        return attPow

    def StrikeEvaded(self):
        global ev, grizz_data, animal
        dodge = round(ev / 10) + round(grizz_data.loc[4, animal] / 10)
        hit = (100 - dodge)

        op = ["Dodge", "Hit"]
        dodged = random.choices(op, weights=(dodge, hit), k=1)
        return dodged

    def Bleeding(self):
        global bleeding, grizz_data, animal
        dmg = grizz_data.loc[15, animal]
        return dmg

    def OppBleed(self):
        global oppBleed
        oppBleed = True
        self.oppBleed = oppBleed
        return oppBleed

    def OppInTree(self):
        global oppInTree
        if self.oppInTree is False:
            self.oppInTree = True
            return self.oppInTree
        else:
            self.oppInTree = False
            return self.oppInTree

    def JungleStatAdj(self):
        global attacks, isCamouflaged
        self.attacks = ["Bite, Punch", "Slam", "Tree Toss"]
        self.ev = self.ev - 25
        self.isCamouflaged = False
        if self.isCamouflaged:
            self.attPT +=1

    def ArcticStatAdj(self):
        global attacks, isCamouflaged
        self.ev = self.ev - 10
        self.speed -= 5
        self.isCamouflaged = False
        if self.isCamouflaged:
            self.attPT +=1

    def DesertStatAdj(self):
        global attacks, isCamouflaged
        self.ev = self.ev - 10
        self.speed -= 5
        self.isCamouflaged = False
        if self.isCamouflaged:
            self.attPT +=1


