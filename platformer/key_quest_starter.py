# KEY QUEST starter. Get the key, then open the door.
# You do NOT need to understand the code above the PART lines.
# You only type your own code under the PART lines.
import turtle

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("skyblue")
screen.title("Key Quest")
screen.tracer(0)
screen.register_shape("key", ((0, -15), (4.2, -13.2), (6, -9), (4.2, -4.8), (2, -3), (2, 14), (-6, 14), (-6, 11), (-2, 11), (-2, 8), (-5, 8), (-5, 5), (-2, 5), (-2, -3), (-4.2, -4.8), (-6, -9), (-4.2, -13.2)))

# ---------- THE WORLD (already built for you) ----------
platforms = []
coins = []


def make_platform(x, y, w, h):
    p = turtle.Turtle()
    p.shape("square")
    p.color("black", "forestgreen")
    p.shapesize(h / 20, w / 20)
    p.penup()
    p.goto(x, y)
    p.half_w = w / 2
    p.top = y + h / 2
    platforms.append(p)


def make_coin(x, y):
    c = turtle.Turtle()
    c.shape("circle")
    c.color("darkorange", "gold")
    c.shapesize(0.7)
    c.penup()
    c.goto(x, y)
    coins.append(c)


make_platform(0, -250, 800, 40)
make_platform(-250, -160, 140, 20)
make_platform(-60, -80, 140, 20)
make_platform(130, 0, 140, 20)
make_platform(300, 80, 140, 20)
make_coin(-250, -120)
make_coin(-60, -40)
make_coin(130, 40)

player = turtle.Turtle()
player.shape("square")
player.color("black", "royalblue")
player.penup()
player.goto(-350, -220)
player.vy = 0
player.on_ground = False
player.has_key = False
player.score = 0

key = turtle.Turtle()
key.shape("key")
key.color("darkgoldenrod", "gold")
key.penup()
key.shapesize(1.4)
key.goto(300, 114)

door = turtle.Turtle()
door.shape("square")
door.color("black", "firebrick")
door.shapesize(3, 2)
door.penup()
door.goto(340, -200)

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.goto(0, 240)


def say(message):
    writer.clear()
    writer.write(message, align="center", font=("Arial", 22, "bold"))


# ---------- THE GAME ENGINE (already built for you) ----------
# These do nothing until YOU replace them in the PART steps.
def check_key():
    pass


def check_door():
    pass


def check_coins():
    pass


def game_loop():
    player.vy = player.vy - 0.8
    player.sety(player.ycor() + player.vy)
    player.on_ground = False
    for p in platforms:
        feet = player.ycor() - 10
        was = feet - player.vy
        if player.vy <= 0 and was >= p.top - 1 and feet <= p.top and abs(player.xcor() - p.xcor()) < p.half_w + 8:
            player.sety(p.top + 10)
            player.vy = 0
            player.on_ground = True
    if player.xcor() < -390:
        player.setx(-390)
    if player.xcor() > 390:
        player.setx(390)
    if player.ycor() < -320:
        player.goto(-350, -220)
        player.vy = 0
    check_key()
    check_door()
    check_coins()
    screen.update()
    screen.ontimer(game_loop, 20)


# ===== PART 2: LEFT AND RIGHT. Type your code under this line =====

# ===== PART 3: JUMPING. Type your code under this line =====

# ===== PART 4: THE KEY. Type your code under this line =====

# ===== PART 5: THE DOOR. Type your code under this line =====

# ===== PART 6: COINS (bonus). Type your code under this line =====

# ===== PART 7: MAKE IT YOURS (bonus). Type your code under this line =====

# ===== Do not type below this line. The game starts here. =====
game_loop()
screen.mainloop()
