import pandas as pd
import random

class Tiger:
    global data,animal, health, speed,bite,punch,slam,attacks,ev,attPT,clawBonus,oppBleed
    data = pd.read_csv("animalfight.csv")
    animal = "TIGER"
    attacks = ["Bite","Claw"]
    speed = data.loc[2, animal]
    bite = data.loc[12, animal]
    punch = data.loc[13, animal]
    health = data.loc[6,animal]
    ev = data.loc[3, animal]
    attPT = round(data.loc[14, animal])
    clawBonus = punch * .2
    oppBleed = False

    def __init__(self):
        global health,speed,bite,punch,slam,attacks,attPT,oppBleed
        self.health = health
        self.speed = speed
        self.attacks = attacks
        self.bite = bite
        self.punch = punch
        self.attPT = attPT
        self.oppBleed = oppBleed



    def RandAttack(self):
        global attacks, clawBonus, bleeding
        att = random.choices(attacks, weights=(40, 60), k=1)
        if att[0] == "Bite":
            hit = random.choices(['T', 'F'], weights=((5), 95))
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
                rB = random.choices(['T', 'F'], weights=(65, 65))
                if rB[0] == "T":
                    self.OppBleed()

        return attPow
    def StrikeEvaded(self):
        global ev, grizz_data, animal
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
t = Tiger()

print(t.bite)