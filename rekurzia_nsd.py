def rek(a: int,b: int):
    if b == 0:
        return a
    else:
        return(rek(b, a%b))
    
a = 145
b = 28

print(rek(a, b))
