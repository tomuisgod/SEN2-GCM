# Sčítanie a odčítanie dvoch matíc

import random

#Tvorenie nahodnej matice
def matica():
    # prazdna maticka
    matica = []
    for i in range(5):
        # generovanie a zapisovanie nahodnych cisel do riadku
        riadok = []
        for j in range(5):
            riadok.append(random.randint(1, 10))
        #vracanie riadku do povodnej matice
        matica.append(riadok)
    return matica

#Scitanie matic
def sucet(m1, m2):
    # prazdna matica (na vysledok)
    vysledok = []
    for i in range(5):
        # scitavanie cisel po riadkoch
        riadok = []
        for j in range(5):
            sucet = m1[i][j] + m2[i][j]
            riadok.append(sucet)
        #vracanie riadku do prazdnej matice
        vysledok.append(riadok)
    return vysledok

#generovanie nahodnej matice
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


vysledok = sucet(m1,m2)

#Vypis vysledku matice
print("#################")
print("Vysledna matica:")
for riadok in vysledok:
    print(riadok)