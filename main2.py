from Dog import Dog
from Cat import Cat

import time
import pickle


def format(x):
    return str(x if len(x) > 0 else "")


filename = "animal.dat"
f = open(filename, 'rb')

farm = pickle.load(f)

cat = set([i for i in range(len(farm)) if farm[i].__class__.__name__ == "Cat"])
dog = set([i for i in range(len(farm)) if farm[i].__class__.__name__ == "Dog"])

fat = set([i for i in range(len(farm)) if farm[i].isFat()])
dead = set([i for i in range(len(farm)) if farm[i].isDead()])
nor = set([i for i in range(len(farm)) if farm[i].isNormal()])

print("Tổng số mèo : {cats}".format(cats=len(cat)))
print("Tổng số chó : {cats}".format(cats=len(dog)))

print("Những con béo : " + format(fat))
print("Những con bình thường : " + format(nor))
print("Những con chết : " + format(dead))
print("Những con mèo béo : " + format(cat.intersection(fat)))
print("Những con mèo bình thường : " + format(cat.intersection(nor)))
print("Những con mèo chêt : " + format(cat.intersection(dead)))
print("Những con chó béo : " + format(dog.intersection(fat)))
print("Những con chó bình thường : " + format(dog.intersection(nor)))
print("Những con chó chết : " + format(dog.intersection(dead)))
print()
f.close()
