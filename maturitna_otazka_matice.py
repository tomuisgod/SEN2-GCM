import random
import tkinter

canvas = tkinter.Canvas(width="300", height="300")

# Pole
a = 3
sp = 300 / a
#Matica
m = []

#Pocet modrych alebo zelenych
z = 0
m_1 = 0

for i in range(3):
    r = []
    for x in range(3):
        num = random.randrange(100)
        r.append(num)
        if num >= 50:
            z += 1
        else:
            m_1 += 1
    m.append(r)
    
for i in range(1, a + 1):
    canvas.create_line(sp * i, 0, sp * i, 700, width=5)
    canvas.create_line(0, sp * i, 700, sp * i, width=5)
    
    """
    canvas.create_line(100*i, 0, 100*i, 700)
    canvas.create_line(0, 100*i, 700, 100*i)
    """

for i in range(3):
    for j in range(3):
        a = m[i][j]
        canvas.create_rectangle(100*i, 100*j, 100*i + 100, 100*j + 100, fill=("green" if a > 50 else "blue"))
        canvas.create_text(100*i + 50, 100*j + 50, text=str(a), fill="black", font=('Helvetica 13 bold'))




print("Zelených: ", z)
print("Modrých: ", m_1)

canvas.pack()
canvas.mainloop()


def baha():
    m = []

    for i in range(3):
        r = []
        for x in range(3):
            r.append(random.randrange(100))
        m.append(r)
    for c in m:
        print("|", end="")
        for x in c:
            print(str(x))
        print("|")
    return m

