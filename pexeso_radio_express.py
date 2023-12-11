import random

pr = []
p = []
pv = []
pexeso = []

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
    pr.append(["0"]*6)

def vypis_pola(a):
    for i in range(len(a)):
        print(a[i])

vypis_pola(pr)
print()
vypis_pola(pexeso)

while True:
    pass
