import tkinter
import random
import string
import time

canvas = tkinter.Canvas(width=1000, height=1000, bg='black')
canvas.pack()

i = 0

def text0():
    global i
    global x
    global y
    if i%27 == 0:
        x = random.randint(10, 1000)
        y = random.randint(10, 1000)
        i = 0
    canvas.create_text(x,50*i, text=random.choice(string.hexdigits + string.ascii_uppercase), fill="green", font=('Helvetica 13 bold'))
    canvas.create_text(y,random.randint(50,100)*i, text=random.choice(string.hexdigits + string.ascii_uppercase), fill="green", font=('Helvetica 13 bold'))

    i += 1
    canvas.after(random.randint(50, 100), text0)
    canvas.update()

text0()

tkinter.mainloop()
