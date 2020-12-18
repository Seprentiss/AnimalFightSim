from SIMS.PLAINS import *
from SIMS.Jungle import *
from SIMS.Desert import *
from SIMS.Arctic import *

def AllSim(animalOne, animalTwo):
    anOneWins = 0
    anTwoWins = 0
    listOfSims = []
    plains = PlainsSim(animalOne, animalTwo)
    listOfSims.append(plains)
    jungle = JungleSim(animalOne, animalTwo)
    listOfSims.append(jungle)
    arctic = ArcticSim(animalOne, animalTwo)
    listOfSims.append(arctic)
    desert = DesertSim(animalOne, animalTwo)
    listOfSims.append(desert)
    for sim in listOfSims:
        anOneWins += sim[0]
        anTwoWins += sim[1]
    return (anOneWins, anTwoWins)