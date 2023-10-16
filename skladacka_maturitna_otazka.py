import random
import tkinter

canvas = tkinter.Canvas(width="300", height="300")

# Pole
a = 3
sp = 300 / a
p = [[1,2,3], [4,5,6], [7,8,""]] 

# Tvorenie pola
for i in range(1, a + 1):
    canvas.create_line(sp * i, 0, sp * i, 700, width=5)
    canvas.create_line(0, sp * i, 700, sp * i, width=5)

for r in range(3):
    for c in range(3):
        a = p[r][c]
        canvas.create_text(100*r + 50, 100*c + 50, text=str(a), fill="Red", font=('Helvetica 20 bold'))

def klik(a):
    print("[ X: ", a.x // 100, "| Y: ", a.y // 100,"]")

    if r+1<3 and p[r+1][c] == 0:
        canvas.move(p[r][c], 100, 0)
        p[r][c],p[r+1][c] = p[r+1][c],p[r][c]

    elif c+1<3 and p[r][c+1] == 0:
        canvas.move(p[r][c], 0, 100)
        p[r][c],p[r][c+1] = p[r][c+1],p[r][c]

    elif r-1>3 and p[r-1][c] == 0:
        canvas.move(p[r][c], -100, 0)
        p[r][c],p[r-1][c] = p[r-1][c],p[r][c]
    elif c-1>3 and p[r][c-1] == 0:
        canvas.move(p[r][c], 0, -100)
        p[r][c],p[r][c-1] = p[r][c-1],p[r][c]

    if p == [[1,2,3], [4,5,6], [7, 8, ""]]:
        canvas.delete("all")
        canvas.create_text(150, 150, text="gg", font="50")
canvas.bind("<Button-1>", klik)

canvas.pack()
canvas.mainloop()
