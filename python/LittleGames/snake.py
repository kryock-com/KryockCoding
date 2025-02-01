import turtle as t
import random
import time

# Game configuration
delay = 0.05
sizeOfHead = 1
score = 0
bodyPartList = []

# Window setup
wn = t.Screen()
wn.setup(width=600, height=600)
wn.title("Snake Game")
wn.bgcolor("black")

# Snake head
head = t.Turtle()
head.shape("circle")
head.shapesize(sizeOfHead)
head.color("green")
head.speed(0)
head.direction = "stop"
head.penup()

# Snake food
food = t.Turtle()
food.shape("turtle")
food.color("brown")
food.speed(0)
food.penup()
food.goto(100, 100)

# Scorekeeper
scorekeeper = t.Turtle()
scorekeeper.hideturtle()
scorekeeper.speed(0)
scorekeeper.penup()
scorekeeper.goto(270, 270)
fontSetting = ("System", 20, "normal")
scorekeeper.write("Score: 0", align="right", font=fontSetting)

# Functions
def up():
    if head.direction != "down":
        head.direction = "up"

def down():
    if head.direction != "up":
        head.direction = "down"

def left():
    if head.direction != "right":
        head.direction = "left"

def right():
    if head.direction != "left":
        head.direction = "right"

def move():
    movementAmount = 20
    if head.direction == "up":
        head.sety(head.ycor() + movementAmount)
    elif head.direction == "down":
        head.sety(head.ycor() - movementAmount)
    elif head.direction == "left":
        head.setx(head.xcor() - movementAmount)
    elif head.direction == "right":
        head.setx(head.xcor() + movementAmount)

def die():
    global score
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"
    score = 0
    scorekeeper.clear()
    scorekeeper.write(f"Score: {score}", align="right", font=fontSetting)
    for bp in bodyPartList:
        bp.goto(random.randint(500, 1000), random.randint(500, 1000))
    bodyPartList.clear()

# Key bindings
wn.listen()
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")

# Main game loop
try:
    while True:
        wn.update()

        # Boundary collision
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            die()

        # Food collision
        if head.distance(food) < 20:
            score += 10
            scorekeeper.clear()
            scorekeeper.write(f"Score: {score}", align="right", font=fontSetting)
            food.goto(random.randint(-280, 280), random.randint(-280, 280))

            newBodyPart = t.Turtle()
            newBodyPart.shape("circle")
            newBodyPart.color("green")
            newBodyPart.speed(0)
            newBodyPart.shapesize(sizeOfHead)
            newBodyPart.penup()
            bodyPartList.append(newBodyPart)

        # Move body parts
        for index in range(len(bodyPartList) - 1, 0, -1):
            x = bodyPartList[index - 1].xcor()
            y = bodyPartList[index - 1].ycor()
            bodyPartList[index].goto(x, y)

        # Move the first body part to the head
        if len(bodyPartList) > 0:
            bodyPartList[0].goto(head.xcor(), head.ycor())

        # Check for collision with body
        for bodyPart in bodyPartList:
            if head.distance(bodyPart) < 20:
                die()

        move()
        time.sleep(delay)

except t.Terminator:
    print("Game exited.")