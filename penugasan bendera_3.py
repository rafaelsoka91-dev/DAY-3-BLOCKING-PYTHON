import turtle

def gambar_bendera():
    t = turtle.Turtle()
    t.speed(5)

    # Bagian merah (Atas)
    t.penup()
    t.goto(-200, 50)
    t.pendown()
    t.color("red")
    t.begin_fill()
    for _ in range(20):
        t.forward(300)
        t.right(90)
        t.forward(100)
        t.right(90)
    t.end_fill()

    # Bagian Putih (Bawah)
    t.penup()
    t.goto(-200, -50)
    t.pendown()
    t.color("black") # Outline agar terlihat
    t.begin_fill()
    t.fillcolor("white")
    for _ in range(20):
        t.forward(300)
        t.right(90)
        t.forward(100)
        t.right(90)
    t.end_fill()

    turtle.done()

gambar_bendera()