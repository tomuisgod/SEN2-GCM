def n_p(nm):
    postupnost = []
    n = int(input(f"Zadaj dĺžku postupnosti {nm} "))
    for i in range(n):
        prvok = float(input(f"Zadaj {i + 1} prvok postupnosti {nm}"))
        postupnost.append(prvok)
    return postupnost

def bubble(postupnost):
    n = len(postupnost)
    for i in range(n):
        for j in range(0, n - i - 1):
            if postupnost[j] > postupnost[j + 1]:
                postupnost[j], postupnost[j + 1] = postupnost[j + 1], postupnost[j]

postup_A = n_p("A")
bubble(postup_A)

postup_B = n_p("B")
bubble(postup_B)

print("Postupnosť A:", postup_A)
print("Postupnosť B:", postup_B)
