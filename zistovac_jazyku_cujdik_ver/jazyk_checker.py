# Kod nie je vo finalnej verzii ku dnesnemu dnu (19. 2. 2024)
# Tento program kontroluje vetu, ktory zadame v inpute. Kontroluje ho takym sposobom, ze kontroluje pismena a rozraduje ich do listu.
# Na zaklade poctu pismen vo vete program zisti, v akom jazyku je tato veta

s = input("...")
pocet_pismen = []
tab = open("doc.txt", "r")
tabulka = []
for i in tab:
    tabulka.append(tab.readline().strip().split(";"))

frektab = [[], [], [], [], []]
for m in range(5):
    for k in range(len(tabulka)):
        frektab[m].append(tabulka[k][m])


for l in range(97, 123):
    pocet = 0
    for j in s:
        if j == chr(l):
            pocet += 1
    pocet_pismen.append(pocet)

print(frektab)
