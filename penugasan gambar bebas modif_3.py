import turtle

t = turtle.Turtle()
t.speed(10)
t.color("black", "purple") # Warna garis dan warna isi

t.begin_fill()
for i in range(10):
    t.forward(200)
    t.right(144)
t.end_fill()

t.hideturtle() #Menyembunyikan kura-kura setelah selesai
turtle.done()