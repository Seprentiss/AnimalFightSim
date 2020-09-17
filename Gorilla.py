import pandas as pd
import random
import math


class Gorilla:
    global g_data, animal, health, speed, bite, punch, slam, attacks, ev, attPT, bleeding, oppBleed, inTree, oppInTree,attPow,isCamouflaged, size, intel
    g_data = pd.read_csv("animalfight.csv")
    animal = "GORILLA"
    attacks = ["Bite", "Slap", "Slam"]
    speed = g_data.loc[2, animal]
    bite = g_data.loc[12, animal]
    intel = g_data.loc[5, animal]
    size = g_data.loc[9, animal]
    punch = (g_data.loc[13, animal])
    slam = punch * 2.25
    health = g_data.loc[6, animal]
    ev = g_data.loc[3, animal]
    attPT = round(g_data.loc[14, animal])
    attPow = 0
    oppBleed = False
    inTree = False
    oppInTree = False
    isCamouflaged = False


    def __init__(self):
        global health, speed, bite, punch, slam, attacks, attPT, oppBleed,inTree, opInTree,isCamouflaged, size, intel
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

    def ClimbTree(self):
        global inTree,attPt,oppInTree
        self.attPT = round(g_data.loc[14, animal])
        if self.inTree is False and oppInTree is False:
            treeClimbed = random.choices(["Yes", "No"], weights=(20, 80))
            if treeClimbed[0] == "Yes":
                self.inTree = True
                self.attPT -= 1
                return self.inTree
            else:
                return self.inTree
        if self.inTree is False and oppInTree is True:
            treeClimbed = random.choices(["Yes", "No"], weights=(70, 30))
            if treeClimbed[0] == "Yes":
                self.inTree = True
                self.attPT -= 1
                return self.inTree
            else:
                return self.inTree
        else:
            treeClimbed = random.choices(["Yes", "No"], weights=(15, 85))
            if treeClimbed[0] == "Yes":
                self.inTree = False
                self.attPT -= 1
                return self.inTree
            else:
                return self.inTree
    def TreeSlamMiss(self):
        self.health -= 300

    def CamoAttack(self):
        global attacks, clawBonus, bleeding, attPow
        hit = random.choices(['T', 'F'], weights=(95, 5))
        if hit[0] == "T":
            self.attPT -= 1
            return "hit"
        else:
            self.attPT -= 1
            return "miss"


    def PlainsRandAttack(self):
        global attacks, bleeding, attPow
        att = random.choices(attacks, weights=(65, 25, 10), k=1)
        if att[0] == "Bite":
            hit = random.choices(['T', 'F'], weights=(4, 96))
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.bite
                rB = random.choices(['T', 'F'], weights=(40, 60))
                if rB[0] == "T":
                    self.OppBleed()
        if att[0] == "Slap":
            hit = random.choices(['T', 'F'], weights=(3, 97))
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.punch
        if att[0] == "Slam":
            hit = random.choices(['T', 'F'], weights=(3, 98))
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.slam
        return attPow

    def JungleRandAttack(self):
        global attacks, bleeding, inTree,oppInTree,attPow
        if self.inTree is True and self.oppInTree is False:
            self.attacks = ["Tree Slam"]
            hit = random.choices(['T', 'F'], weights=(30, 70))
            if hit[0] == "T":
                attPow = 0
                self.TreeSlamMiss()
                self.inTree = False
            else:
                attPow = self.slam * 2.5
            return attPow
        if self.inTree is True and self.oppInTree is True:
            att = random.choices(attacks, weights=(65, 25, 10), k=1)
            if att[0] == "Bite":
                hit = random.choices(['T', 'F'], weights=(10, 90))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.bite
                    rB = random.choices(['T', 'F'], weights=(40, 60))
                    if rB[0] == "T":
                        self.OppBleed()
            if att[0] == "Slap":
                hit = random.choices(['T', 'F'], weights=(10, 90))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.punch
            if att[0] == "Slam":
                hit = random.choices(['T', 'F'], weights=(20, 80))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.slam
            return attPow



        if self.inTree is False and self.oppInTree is True:
            att = random.choices(attacks, weights=(65, 25, 10), k=1)
            if att[0] == "Bite":
                hit = random.choices(['T', 'F'], weights=(100, 0))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.bite
                    rB = random.choices(['T', 'F'], weights=(0, 100))
                    if rB[0] == "T":
                        self.OppBleed()
            if att[0] == "Slap":
                hit = random.choices(['T', 'F'], weights=(100, 0))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.punch
            if att[0] == "Slam":
                hit = random.choices(['T', 'F'], weights=(100, 0))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.slam
            return attPow
        else:
            att = random.choices(attacks, weights=(65, 25, 10), k=1)
            if att[0] == "Bite":
                hit = random.choices(['T', 'F'], weights=(4, 96))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.bite
                    rB = random.choices(['T', 'F'], weights=(40, 60))
                    if rB[0] == "T":
                        self.OppBleed()
            if att[0] == "Slap":
                hit = random.choices(['T', 'F'], weights=(3, 97))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.punch
            if att[0] == "Slam":
                hit = random.choices(['T', 'F'], weights=(3, 97))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.slam
            return attPow

    def ArcticRandAttack(self):
        global attacks, bleeding, attPow
        att = random.choices(attacks, weights=(65, 25, 10), k=1)
        if att[0] == "Bite":
            hit = random.choices(['T', 'F'], weights=(4, 96))
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.bite
                rB = random.choices(['T', 'F'], weights=(40, 60))
                if rB[0] == "T":
                    self.OppBleed()
        if att[0] == "Slap":
            hit = random.choices(['T', 'F'], weights=(3, 97))
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.punch
        if att[0] == "Slam":
            hit = random.choices(['T', 'F'], weights=(3, 98))
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.slam
        return attPow

    def DesertRandAttack(self):
        global attacks, bleeding, attPow
        att = random.choices(attacks, weights=(65, 25, 10), k=1)
        if att[0] == "Bite":
            hit = random.choices(['T', 'F'], weights=(4, 96))
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.bite
                rB = random.choices(['T', 'F'], weights=(40, 60))
                if rB[0] == "T":
                    self.OppBleed()
        if att[0] == "Slap":
            hit = random.choices(['T', 'F'], weights=(3, 97))
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.punch
        if att[0] == "Slam":
            hit = random.choices(['T', 'F'], weights=(3, 98))
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.slam
        return attPow

    def StrikeEvaded(self):
        global ev, g_data, animal
        dodge = round(self.ev / 10) + round(g_data.loc[4, animal] / 10)
        hit = (100 - dodge)
        op = ["Dodge", "Hit"]
        dodged = random.choices(op, weights=(dodge, hit), k=1)
        return dodged

    def Bleeding(self):
        global bleeding, g_data, animal
        dmg = g_data.loc[15, animal]
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
        global attacks
        self.attacks = ["Bite, Punch", "Slam", "Tree Slam"]
        self.ev = self.ev + 50
        self.isCamouflaged = False
        if self.isCamouflaged:
            self.attPT += 1

    def ArcticStatAdj(self):
        global attacks
        self.ev = self.ev -25
        self.speed -= 5
        self.isCamouflaged = False
        if self.isCamouflaged:
            self.attPT += 1

    def DesertStatAdj(self):
        global attacks
        self.attPT = round((((g_data.loc[5, animal] / 5 + g_data.loc[3, animal] / 4) * (g_data.loc[8, animal]-1)) - (math.sqrt(g_data.loc[10, animal]))) / 30)
        self.ev = self.ev -20
        self.speed -= 2
        self.isCamouflaged = False
        if self.isCamouflaged:
            self.attPT += 1



