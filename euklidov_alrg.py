def boohoo(a, b):
    while b:
        a, b = b, a % b
    return a

print("Najvyšší spoločný deliteľ:", boohoo(28, 145))
