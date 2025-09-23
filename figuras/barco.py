import turtle

# --- Ventana ---
screen = turtle.Screen()
screen.setup(600, 400)
screen.bgcolor("skyblue")
screen.title("Barco con bandera clara")

# --- Parámetros (fáciles de ajustar) ---
hull_left, hull_right = -120, 120
hull_top, hull_bottom = -40, -90
mast_x = 0
mast_bottom_y = hull_top + 10
mast_top_y = 120

# --- Agua (fondo inferior) ---
water = turtle.Turtle()
water.hideturtle()
water.penup()
water.goto(-300, hull_bottom - 120)
water.pendown()
water.color("deepskyblue")
water.begin_fill()
water.goto(300, hull_bottom - 120)
water.goto(300, hull_bottom + 20)
water.goto(-300, hull_bottom + 20)
water.goto(-300, hull_bottom - 120)
water.end_fill()
water.penup()

# --- Casco ---
hull = turtle.Turtle()
hull.hideturtle()
hull.penup()
hull.goto(hull_left, hull_top)
hull.pendown()
hull.color("saddlebrown")
hull.fillcolor("sienna")
hull.begin_fill()
hull.goto(hull_right, hull_top)
hull.goto(hull_right - 30, hull_bottom)
hull.goto(hull_left + 30, hull_bottom)
hull.goto(hull_left, hull_top)
hull.end_fill()
hull.penup()

# --- Cubierta ---
deck = turtle.Turtle()
deck.hideturtle()
deck.penup()
deck.goto(hull_left + 20, hull_top)
deck.pendown()
deck.color("peru")
deck.fillcolor("burlywood")
deck.begin_fill()
deck.goto(hull_right - 20, hull_top)
deck.goto(hull_right - 20, hull_top + 12)
deck.goto(hull_left + 20, hull_top + 12)
deck.goto(hull_left + 20, hull_top)
deck.end_fill()
deck.penup()

# --- Mástil ---
mast = turtle.Turtle()
mast.hideturtle()
mast.penup()
mast.goto(mast_x, mast_bottom_y)
mast.pendown()
mast.color("black")
mast.pensize(6)
mast.goto(mast_x, mast_top_y)
mast.penup()

# --- Vela (triángulo unido al mástil) ---
sail = turtle.Turtle()
sail.hideturtle()
sail.penup()
sail.color("white")
sail.fillcolor("white")
# puntos: cima del mástil, base del mástil, punto exterior de la vela
top_point = (mast_x, mast_top_y - 10)
bottom_point = (mast_x, mast_bottom_y + 20)
mid_y = (mast_top_y + mast_bottom_y) / 2
outer_point = (mast_x + 140, mid_y - 10)
sail.goto(top_point)
sail.pendown()
sail.begin_fill()
sail.goto(bottom_point)
sail.goto(outer_point)
sail.goto(top_point)
sail.end_fill()
sail.penup()

# --- Bandera (rectángulo + muesca triangular en color fondo) ---
flag = turtle.Turtle()
flag.hideturtle()
flag.penup()
flag_color = "red"
flag_left = mast_x + 8
flag_width = 50
flag_height = 22
flag_top = mast_top_y + flag_height / 2
flag_bottom = mast_top_y - flag_height / 2

# Rectángulo de la bandera
flag.goto(flag_left, flag_top)
flag.pendown()
flag.color(flag_color)
flag.fillcolor(flag_color)
flag.begin_fill()
flag.goto(flag_left + flag_width, flag_top)
flag.goto(flag_left + flag_width, flag_bottom)
flag.goto(flag_left, flag_bottom)
flag.goto(flag_left, flag_top)
flag.end_fill()
flag.penup()

# Muesca triangular en color de fondo para crear la forma "swallowtail"
flag.goto(flag_left + flag_width, flag_top)
flag.pendown()
flag.color(screen.bgcolor())
flag.fillcolor(screen.bgcolor())
flag.begin_fill()
flag.goto(flag_left + flag_width + 18, mast_top_y)   # punta de la muesca
flag.goto(flag_left + flag_width, flag_bottom)
flag.goto(flag_left + flag_width, flag_top)
flag.end_fill()
flag.penup()

# --- Agujero (ojo) en la cabina para dar más lectura visual ---
port = turtle.Turtle()
port.hideturtle()
port.penup()
port.goto(-40, hull_top + 5)
port.pendown()
port.color("black")
port.fillcolor("lightblue")
port.begin_fill()
port.circle(10)
port.end_fill()
port.penup()

# --- Sol para decorar ---
sun = turtle.Turtle()
sun.hideturtle()
sun.penup()
sun.goto(220, 140)
sun.color("gold")
sun.fillcolor("gold")
sun.pendown()
sun.begin_fill()
sun.circle(30)
sun.end_fill()
sun.penup()

turtle.done()
