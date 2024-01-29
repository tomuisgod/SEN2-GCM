# Vypis najrychlejsieho pretekara

s = open("pretekari.txt")
a = []
m = 999999999

for r in s:
    a.append(r.strip().split(","))
    if m > int(a[-1][2]):
        m = int(a[-1][2])


