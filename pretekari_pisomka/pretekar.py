s = 'doc.txt'
pretekari = {}

# vypis suboru
with open(s, 'r') as subor:
    for riadok in subor:
        hodnoty = riadok.strip().split(', ')
        if len(hodnoty) == 2:
            meno, cas = hodnoty
            pretekari[meno] = int(cas)
        else:
            break #:)

# zoznam pretekarov
print("Pretekári:")
for meno, cas in pretekari.items():
    print(f"{meno}: {cas}")

# porovnavanie casu pretekarov
najrychlejsi_cas = float('inf')
najrychlejsi_meno = None
for meno, cas in pretekari.items():
    if cas < najrychlejsi_cas:
        najrychlejsi_cas = cas
        najrychlejsi_meno = meno
print(f"\nNajrýchlejší pretekár je {najrychlejsi_meno} s časom {najrychlejsi_cas}.")

# porovnanie casu
zotriedeny = sorted(pretekari.values())
rozdiel = zotriedeny[1] - zotriedeny[0]
print(f"Rozdiel medzi prvým a druhým miestom je {rozdiel}.")
