from tqdm import tqdm, trange
from  time import sleep

num = 10000000
for i in trange(num):
    if i == num * .25:
        print("\nLoading Stats ")
    if i == num / 2:
        print("\nPreparing Battle Field")
    if i == num * .75:
        print("\nCalculating Results")
    t = 10
    while t > 0:
        t-= 1

