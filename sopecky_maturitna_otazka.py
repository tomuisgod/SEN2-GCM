import tkinter
import random

canvas = tkinter.Canvas(width=300, height=300)
canvas.pack()

sopka = [0, 300]

# c var urcuje skok
vrcholx = random.randrange(0, 300, 10)

for x in range(0, vrcholx, 10):
    sopka.append(x)
    sopka.append(300-random.randrange(x, x+10))

for x in range(vrcholx, 300, 10):
    sopka.append(x)
    sopka.append(random.randrange(x, x+10))

sopka.append(300)
sopka.append(300)

canvas.create_polygon(sopka)

canvas.mainloop()
