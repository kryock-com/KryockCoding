import turtle as t
import random as rand

courtHeight = 600
courtWidth = 1000
ballSpeed = 12
ballSize=15 
pabbleWidth=60
fontSetting=font=("System", 50, "normal")

wn = t.Screen()
wn.bgcolor("black")
wn.setup(width=1200,height=800)

#redpaddle
redGuy = t.Turtle("square")
redScore = 0
redGuy.speed(0)
redGuy.color("red")
redGuy.penup()
redGuy.setposition(-courtWidth/2,0)
redGuy.turtlesize(5,1)

sRed = t.Turtle(visible=False)
sRed.speed(0)
sRed.color("white")
sRed.penup()
sRed.setposition(-courtWidth/4,courtHeight/4)
sRed.write((str(redScore)),font=fontSetting)

#bluepaddle
blueGuy = t.Turtle("square")
blueScore = 0
blueGuy.speed(0)
blueGuy.color("blue")
blueGuy.penup()
blueGuy.setposition(courtWidth/2,0)
blueGuy.turtlesize(5,1)

sBlue = t.Turtle(visible=False)
sBlue.speed(0)
sBlue.color("white")
sBlue.penup()
sBlue.setposition(courtWidth/4,courtHeight/4)
sBlue.write((str(blueScore)),font=fontSetting)

#ball
ball = t.Turtle("circle")
ball.color("white")
ball.penup()
ball.speed(0)




def drawField():
    #draw the border
    border=t.Turtle(visible=False)#
    border.speed(0)
    border.color("white")
    border.pensize(3)
    border.penup()

    #draw the top border
    border.setposition(-courtWidth/2,courtHeight/2)
    border.pendown()
    border.forward(courtWidth)
    border.penup()
    #draw the bottom border
    border.sety(-courtHeight/2)
    border.pendown()
    border.backward(courtWidth)
    #draw the midcourt line
    border.penup()
    border.setposition(0,courtHeight/2)
    border.pendown()
    border.right(90)
    border.pensize(1)
    #dashes.....
    for i in range(courtHeight//50):
        border.forward(26)
        border.penup()
        border.forward(26)
        border.pendown()

def resetBall():
    ball.setposition(0,0)
    side=rand.randint(0,1)
    if side == 1:
        ball.setheading(rand.randint(-45,45))
    else:
        ball.setheading(rand.randint(135,225))

#bounce
def collideWithPaddle(paddle,b):
    if paddle.distance(b)<ballSize:
        b.setheading(180-b.heading())
        if b.xcor()>0:
            b.setx(b.xcor()-5)
        else:
            b.setx(b.xcor()+5)
        b.forward(ballSpeed)



#move function
def move():
    global blueScore,redScore
    ball.forward(ballSpeed)
    #ball.setheading(90)
    x,y=ball.position()


    if x>courtWidth/2:
        redScore+=1
        sRed.clear()
        sRed.write((str(redScore)),font=fontSetting)        #red scores a point
        resetBall()
    elif x<-courtWidth/2:
        blueScore+=1
        sBlue.clear()
        sBlue.write((str(blueScore)),font=fontSetting)      #blue scores a point
        resetBall()

    elif y>(courtHeight/2-ballSize) or y<(-courtHeight/2+ballSize):     #top and bottom wall collision
        ball.setheading(-ball.heading())
    else:
        collideWithPaddle(redGuy,ball)
        collideWithPaddle(blueGuy,ball)

    wn.ontimer(move,20)

#moving paddles
def upRed():
    y=redGuy.ycor()
    if y<courtHeight/2-pabbleWidth:
        redGuy.sety(y+20)

def downRed():
    y=redGuy.ycor()
    if y>-courtHeight/2+pabbleWidth:
        redGuy.sety(y-20)
    
def upBlue():
    y=blueGuy.ycor()
    if y<courtHeight/2-pabbleWidth:
        blueGuy.sety(y+20)

def downBlue():
    y=blueGuy.ycor()
    if y>-courtHeight/2+pabbleWidth:
        blueGuy.sety(y-20)




wn.onkeypress(resetBall,"r")
wn.onkeypress(upRed,"w")
wn.onkeypress(downRed,"s")
wn.onkeypress(upBlue,"Up")
wn.onkeypress(downBlue,"Down")
wn.listen()

drawField()
move()


wn.mainloop()