import turtle

t = turtle.Turtle()
t.speed(3)

# Lingkaran Luar
t.penup()
t.goto(0, -100)
t.pendown()
t.pensize(5)
t.color("blue")
t.circle(100)

# Teks
t.penup()
t.goto(0, -20)
t.color("black")
t.write("SMK", align="center", font=("Arial", 16, "bold"))
t.goto(0, -50)
t.write("PRESTASI PRIMA", align="center", font=("Arial", 12, "bold"))

t.hideturtle()
turtle.done()