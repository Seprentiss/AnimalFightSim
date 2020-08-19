import pandas as pd
import random
class Bull:
    global data, animal, health, speed, tusk, stomp, horn, attacks, ev, attPT, teethBonus, oppBleed, charge, kick
    data = pd.read_csv("animalfight.csv")
    animal = "BULL"
    attacks = ["Horn", "Charge", "Kick"]
    speed = data.loc[2, animal]
    health = data.loc[6, animal]
    ev = 45
    attPT = round(data.loc[14, animal])
    oppBleed = False
    kick = (data.loc[0, animal] / 2.5) + data.loc[9,animal]
    charge = speed * (data.loc[9, animal] /500) * 3
    print(charge)
    horn = charge / 1.85
    def __init__(self):
        global health, speed, tusk, stomp, slam, attacks, attPT, oppBleed, horn,charge, kick
        self.health = health
        self.speed = speed
        self.attacks = attacks
        self.horn = horn
        self.charge = charge
        self.attPT = attPT
        self.kick = kick
        self.oppBleed = oppBleed

    def RandAttack(self):
        global attacks,teethBonus,bleeding, attPow,horn,charge,kick
        att = random.choices(attacks, weights=(70,15,5), k=1)
        if att[0] == "Horn":
            hit = random.choices(['T','F'], weights=(5,95),k=1)
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.horn
                rB = random.choices(['T','F'], weights=(70,30),k=1)
                if rB[0] == "T":
                    self.OppBleed()
        if att[0] == "Charge":
            hit = random.choices(['T', 'F'], weights=(40, 60))
            if hit[0] == "T":
                attPow = 0
            else:
                attPow = self.charge
        if att[0] == "Kick":
            hit = random.choices(['T', 'F'], weights=(50, 50))
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
        dmg = data.loc[15, animal] + 50
        return dmg


    def OppBleed(self):
        global oppBleed
        oppBleed = True
        self.oppBleed = oppBleed
        return oppBleed

b = Bull()
print(b.RandAttack())