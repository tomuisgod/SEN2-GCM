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