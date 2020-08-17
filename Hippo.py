import pandas as pd
import random
class Hippo:
    global data, animal, health, speed, tusk, stomp, charge, attacks, ev, attPT, teethBonus, oppBleed
    data = pd.read_csv("animalfight.csv")
    animal = "HIPPO"
    attacks = ["Bite", "Charge"]
    speed = data.loc[2, animal]
    health = data.loc[6, animal] / 3
    ev = 0
    attPT = 1
    oppBleed = False
    charge = (speed * (data.loc[9, animal] /500))
    bite = data.loc[12, animal]
    teethBonus = bite * .25

    def __init__(self):
        global health, speed, tusk, stomp, slam, attacks, attPT, oppBleed, charge
        self.health = health
        self.speed = speed
        self.attacks = attacks
        self.charge = charge
        self.attPT = attPT
        self.oppBleed = oppBleed

    def RandAttack(self):
        global attacks,teethBonus,bleeding, attPow
        att = random.choices(attacks, weights=(80,20), k=1)
        if att[0] == "Bite":
            hit = random.choices(['T','F'], weights=(10,95),k=1)
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.bite + teethBonus
                rB = random.choices(['T','F'], weights=(75,25),k=1)
                if rB[0] == "T":
                    self.OppBleed()
        if att[0] == "Charge":
            hit = random.choices(['T', 'F'], weights=(40, 60))
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.charge
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



