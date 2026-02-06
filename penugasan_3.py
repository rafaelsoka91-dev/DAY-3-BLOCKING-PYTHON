import turtle

def draw_flag():
    t = turtle.Turtle()
    
    # Merah
    t.fillcolor("red")
    t.begin_fill()
    for _ in range(2):
        t.forward(200)
        t.left(90)
        t.forward(60)
        t.left(90)
    t.end_fill()
    
    # Putih (pindah ke bawah)
    t.right(90)
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(2):
        t.forward(60)
        t.right(90)
        t.forward(200)
        t.right(90)
    t.end_fill()
    
    turtle.done()

draw_flag()