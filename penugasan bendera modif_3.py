import turtle

def gambar_bendera_terbalik():
    t = turtle.Turtle()
    t.speed(10)

    # --- Bagian PUTIH (Sekarang di Atas) ---
    t.penup()
    t.goto(-150, 100) # Mulai dari posisi lebih tinggi
    t.pendown()
    t.color("black")  # Outline hitam agar warna putih kelihatan
    t.begin_fill()
    t.fillcolor("white")
    for _ in range(2): # Cukup 2 kali perulangan untuk persegi panjang
        t.forward(300)
        t.right(90)
        t.forward(100)
        t.right(90)
    t.end_fill()

    # --- Bagian MERAH (Sekarang di Bawah) ---
    t.penup()
    t.goto(-150, 0)   # Mulai tepat di bawah bagian putih
    t.pendown()
    t.color("red")
    t.begin_fill()
    for _ in range(2):
        t.forward(300)
        t.right(90)
        t.forward(100)
        t.right(90)
    t.end_fill()

    t.hideturtle() # Menyembunyikan kura-kura setelah selesai
    turtle.done()

gambar_bendera_terbalik()