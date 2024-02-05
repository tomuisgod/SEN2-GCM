import tkinter

canvas = tkinter.Canvas(width=1000, height=800)
canvas.pack()

d = 10
s = open("doc.txt", "r")
s_text = s.readline().strip()
a = []
while True:
    for i in range(len(s_text)):
        canvas.create_text(500, 500, text=s_text[i:i+d], tag="o")
        canvas.after(100)
        canvas.update()
        canvas.delete("o")

canvas.create_text()
tkinter.mainloop()
