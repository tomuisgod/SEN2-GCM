# Úloha A
def n_p(nm):
    postupnost = []
    n = int(input(f"Zadaj dĺžku postupnosti {nm}: "))
    for i in range(n):
        prvok = float(input(f"Zadaj {i + 1} prvok postupnosti {nm}: "))
        postupnost.append(prvok)
    return postupnost

# bubble sort
def bubble(postupnost):
    n = len(postupnost)
    for i in range(n):
        for j in range(0, n - i - 1):
            if postupnost[j] > postupnost[j + 1]:
                postupnost[j], postupnost[j + 1] = postupnost[j + 1], postupnost[j]

# Úloha B
def n_p_c(postupn_A, postupn_B):
    if len(postupn_A) < len(postupn_B):
        rozdiel = len(postupn_B) - len(postupn_A)
        postupn_A += [0] * rozdiel
    elif len(postupn_B) < len(postupn_A):
        rozdiel = len(postupn_A) - len(postupn_B)
        postupn_B += [0] * rozdiel

    postupnost_C = []
    for i in range(len(postup_A)):
        postupnost_C.append(postupn_A[i] + postupn_B[i])
    return postupnost_C


def max_med(postupn_C):
    max = float("-inf")
    for prvok in postupn_C:
        if prvok > max:
            max = prvok

    return max

# Volanie funkcii + výpis
postup_A = n_p("A")
bubble(postup_A)

postup_B = n_p("B")
bubble(postup_B)

postup_C = n_p_c(postup_A, postup_B)
bubble(postup_C)

max_C = max_med(postup_C)


print("Postupnosť A:", postup_A)
print("Postupnosť B:", postup_B)
print("Postupnosť C:", postup_C)
print("------------------------")
print("Najväčší prvok v postupnosti C: ", max_C)
