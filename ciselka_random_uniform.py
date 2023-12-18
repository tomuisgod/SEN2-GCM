"""
Maturitná otázka použitím modulu random a funckiue .uniform()... 
Tento spôsob je negelálny a odporúčam array robiť manuálne,
nie pomocou tohto kódu.
"""

import random

neroztriedene = []
neroz_naozaj = []
n = int(input("Zadaj počet čísel: "))

for i in range(n):
    a = round(random.uniform(0.0, 10.0), 1)
    float(a)
    neroztriedene.append(a)

neroz_naozaj = neroztriedene[:]


def bbs_print(a):
    for x in range(len(neroztriedene)):
        for i in range(len(neroztriedene) - 1 - x):
            if neroztriedene[i] > neroztriedene[i + 1]:
                neroztriedene[i], neroztriedene[i + 1] = neroztriedene[i + 1], neroztriedene[i]

    return neroztriedene


def med(a):
    if len(neroztriedene) % 2 == 0:
        return neroztriedene[len(neroztriedene) // 2], neroztriedene[len(neroztriedene) // 2 + 1] / 2
    else:
        return neroztriedene[len(neroztriedene) // 2]


for k in range(neroz_naozaj.index(med(neroztriedene)), 1, -1):
    neroztriedene[k], neroztriedene[k - 1] = neroztriedene[k - 1][k]

def aritmeticky_priemer(a):

    return float(sum(neroztriedene))/float(sum(neroztriedene))

print(med(neroztriedene))
print(bbs_print(neroztriedene))

