import unicodedata
import math

perc = []


with open("pomery_pismen.csv", "r", encoding="utf-8") as e:
    lns = e.readlines()
    for l in lns:
        L = l.split(";")
        perc.append([float(L[1]),float(L[2]),float(L[3]),float(L[4]),float(L[5])])

f = open("doc.txt", "r", encoding="utf-8")
lns = f.readlines()

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

subsidiary_map = {}
for l in lns:
    l = strip_accents(l.lower())
    for m in l:
        if ord(m) not in range(97,123):
            continue
        if m not in subsidiary_map:
            subsidiary_map[m] = 1
        else:
            subsidiary_map[m] = subsidiary_map[m] + 1

infra = 0
for e in subsidiary_map:
    infra += subsidiary_map[e]

percentual_map = {}
for e in subsidiary_map:
    percentual_map[e] = round(subsidiary_map[e]/infra*100,2)

# komplementátor
for i in range(97,123):
    if chr(i) not in percentual_map:
        percentual_map[chr(i)] = 0


# zoradenie
s_percentual_map = {key: value for key, value in sorted(percentual_map.items())}

# komparácia : en=0 fr=1 de=2 cz=3 sk=4
diff = [0, 0, 0, 0, 0]

i = 0
for e in s_percentual_map:
    for j in range(5):
        diff[j] += math.fabs(s_percentual_map[e] - perc[i][j])
    i += 1

min_diff = 0
min_diff_val = 10**7
for d in range(5):
    if diff[d] < min_diff_val:
        min_diff_val = diff[d]
        min_diff = d

if min_diff == 0:
    print("This text is english.")
elif min_diff == 1:
    print("Ce texte est français.")
elif min_diff == 2:
    print("Dieser Text ist deutsch.")
elif min_diff == 3:
    print("Tento text je český.")
elif min_diff == 4:
    print("Tento text je slovenský.")

print(f"\n\nDiferencie textualnych alikvontnych hodnot percipovanych na subjekte: EN = {round(diff[0], 2)} FR = {round(diff[1], 2)} DE = {round(diff[2], 2)} CZ = {round(diff[3], 2)} SK = {round(diff[4], 2)}")
