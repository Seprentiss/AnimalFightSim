import pandas as pd
import random

class Gorilla:
    global g_data, animal, health, speed,bite,punch,slam,attacks,ev,attPT,bleeding,oppBleed
    g_data = pd.read_csv("animalfight.csv")
    animal = "GORILLA"
    attacks = ["Bite","Slap","Slam"]
    speed = g_data.loc[2, animal]
    bite = g_data.loc[12, animal]
    punch = (g_data.loc[13,animal])
    slam = punch * 2.25
    health = g_data.loc[6,animal]
    ev = g_data.loc[3, animal]
    attPT = round(g_data.loc[14, animal])
    oppBleed = False


    def __init__(self):
        global health, speed, bite, punch, slam, attacks, attPT, oppBleed
        self.health = health
        self.speed = speed
        self.attacks = attacks
        self.bite = bite
        self.punch = punch
        self.slam = slam
        self.attPT = attPT
        self.oppBleed = oppBleed



    def RandAttack(self):
        global attacks, bleeding
        att = random.choices(attacks, weights=(65,25,10), k=1)
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
        global ev,g_data,animal
        dodge = round(ev/10) + round(g_data.loc[4, animal] / 10)
        hit = (100 - dodge)
        op = ["Dodge", "Hit"]
        dodged = random.choices(op, weights=(dodge, hit),k=1)
        return dodged

    def Bleeding(self):
        global bleeding, g_data,animal
        dmg = g_data.loc[15, animal]
        return dmg

    def OppBleed(self):
        global oppBleed
        oppBleed = True
        self.oppBleed = oppBleed
        return oppBleed

g = Gorilla()
g.Bleeding()

