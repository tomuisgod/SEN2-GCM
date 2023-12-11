import random

pr = []
p = []
pv = []
pexeso = []
pp = ["A", "B", "C", "D"]

for i in range(1, 13):
    pv.append(i)
    pv.append(i)

for j in range(0, 24):
    a = random.choice(pv)
    p.append(a)
    pv.remove(a)

for i in range(0, 24, 6):
    pexeso.append(p[i:i + 6])

for i in range(4):
    pr.append(["0"] * 6)


def vypis_pola(a):
    for i in range(len(a)):
        print(a[i])


def ukaz_pole():
    vypis_pola(pr)
    print()
    vypis_pola(pexeso)

test = True

while test:
    o = input("Zadaj súradnice npr. A6: ").upper()
    pr[pp.index(o[0])][int(o[1])-1] = pexeso[pp.index(o[0])][int(o[1])-1]
    vypis_pola(pr)

    Q = input("Zadaj súradnice npr. A6: ").upper()
    pr[pp.index(Q[0])][int(Q[1])-1] = pexeso[pp.index(Q[0])][int(Q[1])-1]
    vypis_pola(pr)

    if pexeso[pp.index(Q[0])][int(Q[1])-1] == pexeso[pp.index(o[0])][int(o[1])-1]:
        pass
    else:
        pr[pp.index(o[0])][int(o[1]) - 1] = 0
        pr[pp.index(Q[0])][int(Q[1]) - 1] = 0

    test = False

    for i in range(len(pr)):
        if 0 in pr[i]:
            test = True
            break
