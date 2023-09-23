import random

# Prazdny 3x3 list
matrix = []

# Specifikacia matice
rows = 3
cols = 3
def matrice():
    # Vyplnenie matice nahodnymi cislami od 0 po 10
    for i in range(rows):
        row = []
        for j in range(cols):
            # Nahodne generovanie cisiel do matice a vkladanie ich do listu
            random_value = random.randint(0,10)
            row.append(random_value)
        matrix.append(row)

    # Printovanie matice
    for row in matrix:
        print(row)

def multiplication():
    global row
    
    for x in range(0,3):
        vv = []
        for i in range(0,3):
            vys  = rows * rows
            vv.append[vys]
        print(vv)

multiplication()
