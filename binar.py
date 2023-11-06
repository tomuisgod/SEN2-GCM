a = 11
v = ''

#encrypt
while a > 0:
        b = a % 2
        v += str(b)
        a = a//2
print(v[::-1])

#decrypt
b = [1, 0, 1, 1]
b = b[::-1]
v2 = 0
for i in range(len(b)):
    v2 += b[-(i+1)]*2**i
print(v2)
