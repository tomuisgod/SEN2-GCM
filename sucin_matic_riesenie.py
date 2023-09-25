import random

def sucet(x, z):
    policko = []
    pole = []

    for n in range(x):
        for i in range(z):
            a = random.randrange(0, 10)
            policko.append(a)
        pole.append(policko)
        policko = []
    return(pole)  

t = sucet(3, 3)
j = sucet(3, 3)

def sucet_matic(mat1, mat2):    
    p = []
    for x in range(len(mat1)):
        p_p = []
        for i in range(len(mat1)):
            vys = t[x][i] +  j[x][i]
            p_p.append(vys)
        p.append(p_p)
    return(p)
    
def vypis(d):
    for i in range(len(d)):
        print(d(i))

def nasobenie_vp(mat1, mat2):
    p = []
    for x in range(len(mat1)):
        p_p = []
        for i in range(len(mat1)):
            vys = t[x][i] *  j[x][i]
            p_p.append(vys)
        p.append(p_p)
    return(p)

vypis(sucet_matic(t, j))
vypis(nasobenie_vp(t, j))

