import random

def sucet(x, z):
    policko = []
    pole = []

    for n in range(x):
        for i in range(z):
            a = random.randrange(0, 10)
            policko.append(a)
        pole.append(policko)
        policko = []
    return print(pole)  

t = sucet(8, 8)
j = sucet(8, 8)

for x in range(len(t)):
    for i in range(len(t)):
        vys = t[0][i]+[0][i]
        pp.append(vys)
    pp = []

print(pp) 
