import pandas as pd
import random

class Elephant:
    global data, animal, health, speed, tusk, stomp, ram, attacks, ev, attPT, clawBonus, oppBleed
    data = pd.read_csv("animalfight.csv")
    animal = "ELEPHANT"
    attacks = ["Tusk", "Stomp", "Ram"]
    speed = data.loc[2, animal]
    health = data.loc[6, animal]
    ev = 0
    attPT = 1
    oppBleed = False
    stomp = data.loc[13, animal]
    tusk = (data.loc[0, animal]/10) + (speed/10) * (stomp / 1000)
    ram = speed * (data.loc[9, animal] /500)

    def __init__(self):
        global health, speed, tusk, stomp, slam, attacks, attPT, oppBleed, ram
        self.health = health
        self.speed = speed
        self.attacks = attacks
        self.tusk = tusk
        self.stomp = stomp
        self.ram = ram
        self.attPT = attPT
        self.oppBleed = oppBleed

    def RandAttack(self):
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



e = Elephant()

print(e.tusk, e.ram, e.stomp)
print(e.RandAttack())
