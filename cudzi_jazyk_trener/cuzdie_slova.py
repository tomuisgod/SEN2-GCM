import random

with open("doc.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

count = 0

while True:
    random_line = random.choice(lines)
    slovicko, odpoved = random_line.strip().split(":")
    print(slovicko)
    guess = input(" ").strip().lower()

    if guess == odpoved:
        count += 1
        print("Správne, pokračujte ďalej.")
        print("Počet správnych odpovedí:", count)
        print("________________________")
    else:
        print("Bohužiaľ, nesprávne. Správna odpoveď je:", odpoved)
        print("Počet správnych odpovedí:", count)
        print("________________________")

    if guess == "-":
        break
