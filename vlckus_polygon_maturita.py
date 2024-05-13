import tkinter

canvas = tkinter.Canvas(width=1000, height=1000)
n = int(input("Zadajte pocet trojuholnikov: "))

while n > 0:
    canvas.create_polygon(499, 300-n*60, 328-n*52, 600+n*31, 675+n*51, 600+n*28, fill="white", outline="black")
    n -= 1

canvas.pack()
canvas.mainloop()

input("")
