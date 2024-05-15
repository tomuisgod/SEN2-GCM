"""
Prvočíslo se nazývá permutovateľné, ak zostáva prvočíslom, aj keď zameníme poradie jeho cifier tj. permutujeme jeho cifry) ľubovoľným spôsobom. 
Napríklad 13 je permutovateľné prvočíslo, protože 13 aj 31 sú prvočísla, podobne 113 je permutovateľné prvočíslo (lebo 113, 131 i 311 sú prvočísla). 
Naopak prvočíslo 03 nie je permutovateľné, pretože 130 nie je rvočíslo. Nájdite a vypíšte všetky ermutovateľné prvočísla menšie ako 1000.
"""

def prvocislo(x):

    for i in range(2,x):

        if x % i == 0:
            return False

    return True


def perm(number):
    current_perm = ['']
    final_perm = []

    for digit in number:
        next_perm = []

        for perm in current_perm:

            for i in range(len(perm)+1):
                next_perm.append(perm[:i]+digit+perm[i:])

        current_perm = next_perm

    for number in current_perm:

        if number != "0" or number not in final_perm:

            final_perm.append(int(number))

    return(final_perm)

result = []

for n in range(10,1000):
    is_perm = True

    if prvocislo(n):

        for number in perm(str(n)):

            if prvocislo(number) == False:
                
                is_perm = False

        if is_perm:
            result.append(n)

print(result)