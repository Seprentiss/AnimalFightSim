from tqdm import tqdm, trange
from  time import sleep

att1 = 5
att2 = 1

oneH = 10
twoH = 47

end = False

if att1 > att2:
    tot = att1
else:
    tot = att2

while ((oneH > 0 or twoH > 0) and end is False):
    att1 = 5
    att2 = 1
    if att1 > att2:
        tot = att1
    else:
        tot = att2
    for t in range(tot):
        if att1 > 0:
            twoH -= 1
            att1 = att1 - 1
            if twoH <= 0:
                print("one wins")
                end = True
                break
        if att2 > 0:
            oneH -= 1
            att2 = att2 - 1
            if oneH <= 0:
                print("two wins")
                end = True
                break
