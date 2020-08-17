import pandas as pd
import random

class Grizzly:
    global grizz_data,animal, health, speed,bite,punch,slam,attacks,ev,attPT,clawBonus,bleeding
    grizz_data = pd.read_csv("animalfight.csv")
    animal = "GRIZZLY BEAR"
    attacks = ["Bite","Claw", "Slam"]
    speed = grizz_data.loc[2, animal]
    bite = grizz_data.loc[12, animal]
    punch = (grizz_data.loc[9,animal] / 5) * (grizz_data.loc[0,animal] / 100) + (grizz_data.loc[5,animal] / 10)
    slam = punch * 1.5
    health = grizz_data.loc[6,animal]
    ev = grizz_data.loc[3, animal]
    attPT = round(grizz_data.loc[14, animal])
    clawBonus = 150

    def __init__(self):
        global health,speed,bite,punch,slam,attacks,attPT,bleeding
        self.health = health
        self.speed = speed
        self.attacks = attacks
        self.bite = bite
        self.punch = punch
        self.slam = slam
        self.attPT = attPT
        self.bleeding = bleeding


    def getSpeed(self):
        return self.speed
    def getAttcks(self):
        return self.attacks
    def getBite(self):
        return self.bite
    def getPunch(self):
        return self.punch
    def getSlam(self):
        return self.slam
    def getAttPT(self):
        return self.attPT

    def RandAttack(self):
        global attacks,clawBonus,bleeding
        att = random.choices(attacks, weights=(55, 35, 10), k=1)
        if att[0] == "Bite":
            attPow = self.bite
        if att[0] == "Claw":
            attPow = self.punch + clawBonus
        if att[0] == "Slam":
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
        global bleeding
        bleeding = True
        self.attPT -= 1



