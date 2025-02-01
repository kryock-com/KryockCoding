import turtle as t
import random as rand

# Configuration
courtHeight = 600
courtWidth = 1000
ballSpeed = 12
ballSize = 15
paddleWidth = 60
fontSetting = ("System", 50, "normal")

# Initialize screen
wn = t.Screen()
wn.bgcolor("black")
wn.setup(width=1200, height=800)

# Red paddle
redGuy = t.Turtle("square")
redScore = 0
redGuy.speed(0)
redGuy.color("red")
redGuy.penup()
redGuy.setposition(-courtWidth / 2 + 20, 0)
redGuy.turtlesize(5, 1)

sRed = t.Turtle(visible=False)
sRed.speed(0)
sRed.color("white")
sRed.penup()
sRed.setposition(-courtWidth / 4, courtHeight / 4)
sRed.write(str(redScore), font=fontSetting)

# Blue paddle (computer)
computer = t.Turtle("square")
computerScore = 0
computer.speed(0)
computer.color("blue")
computer.penup()
computer.setposition(courtWidth / 2 - 20, 0)
computer.turtlesize(5, 1)

sComputer = t.Turtle(visible=False)
sComputer.speed(0)
sComputer.color("white")
sComputer.penup()
sComputer.setposition(courtWidth / 4, courtHeight / 4)
sComputer.write(str(computerScore), font=fontSetting)

# Ball
ball = t.Turtle("circle")
ball.color("white")
ball.penup()
ball.speed(0)

# Draw field
def drawField():
    border = t.Turtle(visible=False)
    border.speed(0)
    border.color("white")
    border.pensize(3)
    border.penup()

    # Draw top and bottom borders
    border.setposition(-courtWidth / 2, courtHeight / 2)
    border.pendown()
    border.forward(courtWidth)
    border.penup()
    border.sety(-courtHeight / 2)
    border.pendown()
    border.backward(courtWidth)

    # Draw midcourt line
    border.penup()
    border.setposition(0, courtHeight / 2)
    border.pendown()
    border.right(90)
    border.pensize(1)
    for _ in range(courtHeight // 50):
        border.forward(26)
        border.penup()
        border.forward(26)
        border.pendown()

# Reset ball position and direction
def resetBall():
    ball.setposition(0, 0)
    side = rand.choice([1, -1])
    ball.setheading(rand.randint(-45, 45) * side)

# Paddle collision
def collideWithPaddle(paddle, b):
    px, py = paddle.position()
    bx, by = b.position()

    if (px - 10 <= bx <= px + 10) and (py - 50 <= by <= py + 50):
        b.setheading(180 - b.heading())
        b.forward(ballSpeed)

# Move ball
def move():
    global computerScore, redScore

    ball.forward(ballSpeed)
    x, y = ball.position()

    # Computer paddle movement (limited reaction speed)
    if computer.ycor() < ball.ycor() and computer.ycor() < courtHeight / 2 - paddleWidth:
        computer.sety(computer.ycor() + 10)
    elif computer.ycor() > ball.ycor() and computer.ycor() > -courtHeight / 2 + paddleWidth:
        computer.sety(computer.ycor() - 10)

    # Scoring
    if x > courtWidth / 2:
        redScore += 1
        sRed.clear()
        sRed.write(str(redScore), font=fontSetting)
        resetBall()
    elif x < -courtWidth / 2:
        computerScore += 1
        sComputer.clear()
        sComputer.write(str(computerScore), font=fontSetting)
        resetBall()

    # Wall collision
    if y > (courtHeight / 2 - ballSize) or y < (-courtHeight / 2 + ballSize):
        ball.setheading(-ball.heading())

    # Paddle collision
    collideWithPaddle(redGuy, ball)
    collideWithPaddle(computer, ball)

    wn.ontimer(move, 20)

# Red paddle movement
def upRed():
    if redGuy.ycor() < courtHeight / 2 - paddleWidth:
        redGuy.sety(redGuy.ycor() + 20)

def downRed():
    if redGuy.ycor() > -courtHeight / 2 + paddleWidth:
        redGuy.sety(redGuy.ycor() - 20)

# Key bindings
wn.onkeypress(resetBall, "r")
wn.onkeypress(upRed, "w")
wn.onkeypress(downRed, "s")
wn.listen()

# Start game
drawField()
resetBall()
move()
wn.mainloop()