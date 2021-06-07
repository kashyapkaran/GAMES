#colorsquarespiral2.py
iimport turtle
t = turtle.Pen()
t.speed(0)
ssides = 8
ccolors = ["red","yellow","blue","green","purple","  light blue"," gold","orange"]

ffor x in range(360):
    t.pencolor(colors[ x % sides])
    t.forward(2*x)
    t.left(360/sides + 1)
    t.width(x*sides/100)
