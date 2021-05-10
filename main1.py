from Dog import Dog
from Cat import Cat
import random
import time
import pickle

random.seed(32)
n = 100
t = 6
filename = "animal.dat"

farm = []

for i in range(n):
    r = random.randrange(0, 2)
    farm.append(Dog() if r == 0 else Cat())

day = 1
while day <= t:
    print("day {day}:".format(day=day))
    for animal in farm:
        animal.hurry()
    eat = random.sample(range(n), n*3//10)
    for i in eat:
        farm[i].eat()
    day += 1
    file_animal = open(filename, 'wb')
    pickle.dump(farm, file_animal)
    time.sleep(1)

file_animal.close()
