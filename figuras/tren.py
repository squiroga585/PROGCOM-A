import turtle

# --- Ventana ---
screen = turtle.Screen()
screen.setup(900, 400)
screen.bgcolor("lightsteelblue")
screen.title("Tren sencillo con Turtle")

def make_turtle():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    return t

# --- Vías ---
rails = make_turtle()
rails.goto(-420, -120)
rails.pendown()
rails.color("saddlebrown")
rails.pensize(6)
rails.forward(840)  # riel superior
rails.penup()

rails.goto(-420, -140)
rails.pendown()
rails.forward(840)  # riel inferior
rails.penup()

# durmientes
sleepers = make_turtle()
sleepers.color("peru")
x = -380
while x < 380:
    sleepers.goto(x, -135)
    sleepers.setheading(0)
    sleepers.pendown()
    sleepers.begin_fill()
    for _ in range(2):
        sleepers.forward(50)
        sleepers.right(90)
        sleepers.forward(6)
        sleepers.right(90)
    sleepers.end_fill()
    sleepers.penup()
    x += 60

# --- Función para rectángulo ---
def draw_box(x, y, w, h, fill):
    t = make_turtle()
    t.goto(x, y)
    t.pendown()
    t.color("black")
    t.fillcolor(fill)
    t.begin_fill()
    for _ in range(2):
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)
    t.end_fill()
    t.penup()

# --- Locomotora ---
draw_box(-360, -50, 160, 80, "firebrick")   # cuerpo
draw_box(-280, -80, 80, -80, "maroon")       # cabina superior
draw_box(-320, -35, 40, 40, "dimgray")     # frente (simula motor)

# --- Vagones ---
draw_box(-180, -50, 140, 80, "darkorange")
draw_box(-20, -50, 140, 80, "goldenrod")

# --- Ruedas ---
def draw_wheel(cx, cy, r=18):
    w = make_turtle()
    w.goto(cx, cy - r)
    w.pendown()
    w.color("black")
    w.fillcolor("black")
    w.begin_fill()
    w.circle(r)
    w.end_fill()
    w.penup()

# ruedas locomotora
draw_wheel(-330, -135, 18)
draw_wheel(-260, -135, 18)

# ruedas vagón 1
draw_wheel(-140, -135, 18)
draw_wheel(-80, -135, 18)

# ruedas vagón 2
draw_wheel(20, -135, 18)
draw_wheel(80, -135, 18)

# --- Ventanas en vagones ---
win = make_turtle()
for x in range(-160, 60, 40):  # vagón 1
    win.goto(x, 0)
    win.pendown()
    win.color("black")
    win.fillcolor("white")
    win.begin_fill()
    win.circle(10)
    win.end_fill()
    win.penup()

for x in range(0, -100, 40):  # vagón 2
    win.goto(x, 0)
    win.pendown()
    win.begin_fill()
    win.circle(10)
    win.end_fill()
    win.penup()

# --- Chimenea ---
chim = make_turtle()
chim.goto(-330, -10)
chim.pendown()
chim.color("black")
chim.fillcolor("dimgray")
chim.begin_fill()
for _ in range(2):
    chim.forward(20)
    chim.right(90)
    chim.forward(40)
    chim.right(90)
chim.end_fill()
chim.penup()

# --- Humo ---
smoke = make_turtle()
smoke.color("lightgray")
for dx, dy, r in [(-318, 10, -5), (-308, 20, 14), (-250, 18, 18)]:
    smoke.goto(dx, dy)
    smoke.pendown()
    smoke.begin_fill()
    smoke.circle(r)
    smoke.end_fill()
    smoke.penup()

turtle.done()
