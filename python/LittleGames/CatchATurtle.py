# a121_catch_a_turtle.py
#-----import statements-----
import turtle as t
import random as rand
import leaderboard as lb

#-----game configuration----

leaderboardFileName='a122_leaderboard.txt'
#if you get an error that says no such file found:
#   1. spelling
#   2. same folder
#   3. Google it

leaderNamesList=[]
leaderScoresList=[]
playerNames = t.textinput("Player Name", "Enter your name:")

spotColor = "red"
spotSize = 2
spotShape = "turtle"
timer = 30  # Adjusted timer for longer gameplay
counterInterval = 1000
timerUp = False

score = 0
fontSetting = ("Arial", 16, "normal")  # Font settings

#-----initialize turtle-----
spot = t.Turtle()
spot.shape(spotShape)
spot.shapesize(spotSize)
spot.fillcolor(spotColor)

scoreKeeper = t.Turtle()
scoreKeeper.hideturtle()
scoreKeeper.penup()
scoreKeeper.goto(150, 180)
scoreKeeper.pendown()

counter = t.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-150, 180)
counter.pendown()

#-----game functions--------
def spotClicked(x, y):
    global timerUp
    if not timerUp:
        changePosition()
        updateScore()
    else:
        spot.hideturtle()

def changePosition():
    newX, newY = rand.randint(-173, 173), rand.randint(-173, 173)
    spot.penup()
    spot.hideturtle()
    spot.goto(newX, newY)
    spot.showturtle()
    spot.pendown()

def updateScore():
    global score
    score += 1
    scoreKeeper.clear()
    scoreKeeper.write(("Score: " + str(score)), font=fontSetting)

def countdown():
    global timer, timerUp
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up!", font=fontSetting)
        timerUp = True
        manage_leaderboard()
    else:
        counter.write("Timer: " + str(timer), font=fontSetting)
        timer -= 1
        counter.getscreen().ontimer(countdown, counterInterval)

def manage_leaderboard():
    global leaderScoresList, leaderNamesList, score, spot

    # Load leaderboard records into lists
    lb.load_leaderboard(leaderboardFileName, leaderNamesList, leaderScoresList)

    # Check if the score qualifies for the leaderboard
    if len(leaderScoresList) < 5 or score > leaderScoresList[-1]:
        lb.update_leaderboard(leaderboardFileName, leaderNamesList, leaderScoresList, playerNames, score)
        lb.draw_leaderboard(leaderNamesList, leaderScoresList, True, spot, score)
    else:
        lb.draw_leaderboard(leaderNamesList, leaderScoresList, False, spot, score)

#-----events----------------
spot.onclick(spotClicked)
wn = t.Screen()
wn.bgcolor("light blue")
wn.ontimer(countdown, counterInterval)
wn.mainloop()