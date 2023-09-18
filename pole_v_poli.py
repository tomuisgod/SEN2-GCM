import random

# Moja alternativa
def jedna():
    a = []

    for i in range(0,3):
        n = random.sample(range(0, 10), 3)
        a.append(n)
    return print(a)

# Cujdikova alternativa
def dva(x: int, z: int):
    policko = []
    pole = []

    for n in range(x):
        for i in range(z):
            a = random.randrange(0, 10)
            policko.append(a)
        pole.append(policko)
        policko = []
    return print(pole)

jedna()
dva(5, 2)
