import turtle

t = turtle.Turtle()
t.speed(5)
t.color("orange", "yellow") # Warna garis dan warna isi

t.begin_fill()
for i in range(5):
    t.forward(200)
    t.right(144)
t.end_fill()

turtle.done()