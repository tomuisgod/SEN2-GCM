# Sčítanie a odčítanie dvoch matíc

import random

#Tvorenie nahodnej matice
def matica():
    matica = []
    for i in range(5):
        riadok = []
        for j in range(5):
            riadok.append(random.randint(1, 10))
        matica.append(riadok)
    return matica

#Scitanie matic
def odpocet(m1, m2):
    vysledok = []
    for i in range(5):
        riadok = []
        for j in range(5):
            odcitanie = m1[i][j] - m2[i][j]
            riadok.append(odcitanie)
        vysledok.append(riadok)
    return vysledok

m1 = matica()
m2 = matica()


#Vypis matic
print("matica 1:")
for riadok in m1:
    print(riadok)

print("#################")

print("matica 2:")
for riadok in m2:
    print(riadok)

vysledok = odpocet(m1,m2)

print("#################")
print("Vysledna matica:")
for riadok in vysledok:
    print(riadok)