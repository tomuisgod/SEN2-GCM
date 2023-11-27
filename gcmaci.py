import random

kyseliny = ['a', 'c', 't', 'g', 'u']


def krasa_gcmaka(gcmak):
    eugenika = 0
    for i in range(5):
        if gcmak[i] == kyseliny[i]:
            eugenika += 1
    return eugenika


def avg_krasa(gcmaci):
    sucet_kras = 0
    for gcmak in gcmaci:
        sucet_kras += krasa_gcmaka(gcmak)
    return sucet_kras / len(gcmaci)


gcmaci = []
for i in range(400):
    gcmaci.append([random.choice(kyseliny), random.choice(kyseliny), random.choice(kyseliny), random.choice(kyseliny),
                   random.choice(kyseliny)])

index_generacie = 1
while len(gcmaci) != 1:
    print(index_generacie, avg_krasa(gcmaci))
    neo_gcmaci = []
    pary = []
    for gcmak in gcmaci:
        if krasa_gcmaka(gcmak) < avg_krasa(gcmaci):
            gcmaci.remove(gcmak)
        else:
            gcmaci.remove(gcmak)
            gcmacka = random.choice(gcmaci)
            while krasa_gcmaka(gcmacka) < avg_krasa(gcmaci):
                gcmaci.remove(gcmacka)
                gcmacka = random.choice(gcmaci)
            pary.append((gcmak, gcmacka))
            gcmaci.remove(gcmacka)

    for par in pary:
        neo_gcmak = []
        for i in range(5):
            neo_gcmak.append(random.choice(par)[i])
        if random.randrange(100) <= 8:
            neo_gcmak[random.randrange(5)] = random.choice(kyseliny)
        neo_gcmaci.append(neo_gcmak)

    gcmaci = neo_gcmaci
    index_generacie += 1

print(gcmaci)
print(krasa_gcmaka(gcmaci[0]))
