maximum = float('inf')
submaximum = -1
pretekar = ""

with open("doc.txt", mode="r", encoding="utf-8") as f: 
    for i in f.readlines():
        isp = i.split(", ")
        ksp = int(isp[1].strip())
        if ksp < maximum:
            submaximum = maximum
            maximum = ksp 
            pretekar = isp[0]

print(f"Najrýchlejší: {pretekar} ({maximum-submaximum} s)")



