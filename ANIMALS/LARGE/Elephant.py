import pandas as pd
import random

class Elephant:
    global data, animal, health, speed, tusk, stomp, ram, attacks, ev, attPT, clawBonus, oppBleed,inTree,oppInTree,attPow,isCamouflaged, size, intel
    data = pd.read_csv("/Users/spencerprentiss/PycharmProjects/AnimalFightSimulator/animalfight(3).csv")
    animal = "ELEPHANT"
    attacks = ["Tusk", "Stomp", "Ram"]
    speed = data.loc[2, animal]
    intel = data.loc[5, animal]
    size = data.loc[9, animal]
    health = data.loc[6, animal]
    ev = data.loc[3, animal]
    attPT = round(data.loc[14, animal])
    oppBleed = False
    stomp = data.loc[13, animal]
    tusk = (data.loc[0, animal]/10) + (speed/10) * (stomp / 20)
    ram = speed * (data.loc[9, animal] /10)
    inTree = False
    oppInTree = False
    attPow = 0
    isCamouflaged = False

    def __init__(self):
        global health, speed, tusk, stomp, slam, attacks, attPT, oppBleed, ram,isCamouflaged, size, intel
        self.health = health
        self.speed = speed
        self.size = size
        self.intel = intel
        self.attacks = attacks
        self.tusk = tusk
        self.stomp = stomp
        self.ram = ram
        self.attPT = attPT
        self.oppBleed = oppBleed
        self.ev = ev
        self.inTree = inTree
        self.oppInTree = oppInTree
        self.isCamouflaged = isCamouflaged
        self.aggression = data.loc[16, animal]

    def ClimbTree(self):
        global inTree, attPt
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
        global attacks,clawBonus,bleeding, attPow
        att = random.choices(attacks, weights=(70, 5, 25), k=1)
        if att[0] == "Tusk":
            hit = random.choices(['T','F'], weights=(60, 40),k=1)
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.tusk
                rB = random.choices(['T','F'], weights=(40,60),k=1)
                if rB[0] == "T":
                    self.OppBleed()
        if att[0] == "Stomp":
            hit = random.choices(['T', 'F'], weights=(98 , 2),k=1)
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.stomp
        if att[0] == "Ram":
            hit = random.choices(['T', 'F'], weights=(70, 30))
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.ram
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
            att = random.choices(attacks, weights=(70, 5, 25), k=1)
            if att[0] == "Tusk":
                hit = random.choices(['T', 'F'], weights=(100, 0))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.tusk
                    rB = random.choices(['T', 'F'], weights=(40, 60))
                    if rB[0] == "T":
                        self.OppBleed()
            if att[0] == "Stomp":
                hit = random.choices(['T', 'F'], weights=(100, 0))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.stomp
            if att[0] == "Ram":
                hit = random.choices(['T', 'F'], weights=(100, 0))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.ram
            return attPow
        if self.inTree is False and oppInTree is True:
            att = random.choices(attacks, weights=(70, 5, 25), k=1)
            if att[0] == "Tusk":
                hit = random.choices(['T', 'F'], weights=(100, 0))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.tusk
                    rB = random.choices(['T', 'F'], weights=(40, 60))
                    if rB[0] == "T":
                        self.OppBleed()
            if att[0] == "Stomp":
                hit = random.choices(['T', 'F'], weights=(100, 0))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.stomp
            if att[0] == "Ram":
                hit = random.choices(['T', 'F'], weights=(100, 0))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.ram
            return attPow
        else:
            att = random.choices(attacks, weights=(70, 5, 25), k=1)
            if att[0] == "Tusk":
                hit = random.choices(['T', 'F'], weights=(75, 25), k=1)
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.tusk
                    rB = random.choices(['T', 'F'], weights=(40, 60), k=1)
                    if rB[0] == "T":
                        self.OppBleed()
            if att[0] == "Stomp":
                hit = random.choices(['T', 'F'], weights=(98, 2), k=1)
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.stomp
            if att[0] == "Ram":
                hit = random.choices(['T', 'F'], weights=(80, 20))
                if hit[0] == "T":
                    attPow = 0
                else:
                    attPow = self.ram
            return attPow

    def ArcticRandAttack(self):
        global attacks,clawBonus,bleeding, attPow
        att = random.choices(attacks, weights=(70, 5, 25), k=1)
        if att[0] == "Tusk":
            hit = random.choices(['T','F'], weights=(65, 45),k=1)
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.tusk
                rB = random.choices(['T','F'], weights=(40,60),k=1)
                if rB[0] == "T":
                    self.OppBleed()
        if att[0] == "Stomp":
            hit = random.choices(['T', 'F'], weights=(98 , 2),k=1)
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.stomp
        if att[0] == "Ram":
            hit = random.choices(['T', 'F'], weights=(80, 20))
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.ram
        return attPow

    def DesertRandAttack(self):
        global attacks,clawBonus,bleeding, attPow
        att = random.choices(attacks, weights=(75, 5, 20), k=1)
        if att[0] == "Tusk":
            hit = random.choices(['T','F'], weights=(65, 45),k=1)
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.tusk
                rB = random.choices(['T','F'], weights=(40,60),k=1)
                if rB[0] == "T":
                    self.OppBleed()
        if att[0] == "Stomp":
            hit = random.choices(['T', 'F'], weights=(98 , 2),k=1)
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.stomp
        if att[0] == "Ram":
            hit = random.choices(['T', 'F'], weights=(80, 20))
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.ram
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
        self.ev = 0
        self.speed -= 10
        self.isCamouflaged = False
        if self.isCamouflaged:
            self.attPT += 1

    def ArcticStatAdj(self):
        self.ev = 0
        self.speed -= 15
        self.isCamouflaged = False
        if self.isCamouflaged:
            self.attPT += 1

    def DesertStatAdj(self):
        self.ev = 0
        self.speed -= 15
        self.isCamouflaged = False
        if self.isCamouflaged:
            self.attPT += 1




