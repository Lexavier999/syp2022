import turtle
import time
import random
import math
import itertools

screen = turtle.Screen()
screen.tracer(0)
screen.title("Platforming")
screen.setup(width=1880, height=980)

player = turtle.Turtle()
player.shape("square")
player.color("pink")
player.penup()
player.turtlesize(4)
player.goto(0,0)
player.yV = 0
player.xV = 0
x = player.xcor()
y = player.ycor()

floor = turtle.Turtle()
floor.shape("square")
floor.color("black")
floor.penup()
floor.goto(0,0)

leftwall = turtle.Turtle()
leftwall.shape("square")
leftwall.color("red")
leftwall.penup()
leftwall.goto(0,0)

rightwall = turtle.Turtle()
rightwall.shape("square")
rightwall.color("yellow")
rightwall.penup()
rightwall.goto(0,0)

inair = True
Jumps = 0

def jump():
    global Jumps, inair
    if Jumps < 2:
        inair = True
        player.yV = +15
        Jumps+=1

def collision():
    global Jumps, y, x, inair, jumptiles, walltiles
    jdistances = []
    lwdistances = []
    rwdistances = []
    validtiles = []

    y = player.ycor()
    x = player.xcor()
    for i in jumptiles:
        jdistances.append(player.distance(i))
    for j in lwalltiles:
        lwdistances.append(leftwall.distance(j))
    for o in rwalltiles:
        rwdistances.append(rightwall.distance(o))

    minjdisindex = jdistances.index(min(jdistances))
    minjtile = jumptiles[minjdisindex]
    minlwdisindex = lwdistances.index(min(lwdistances))
    minlwtile = lwalltiles[minlwdisindex]
    minrwdisindex = rwdistances.index(min(rwdistances))
    minrwtile = rwalltiles[minrwdisindex]

    if (int(minjtile.ycor())+40) < player.ycor():
        floor.goto(player.xcor(), (int(minjtile.ycor())+40))
    else:
        floor.goto(player.xcor(), player.ycor()-40)
    if int(player.distance(minjtile)) < 94:
        if y < int(floor.ycor()+40) and y > int(floor.ycor()+15):
            player.yV = 0
            player.sety(int(floor.ycor())+40)
            Jumps = 0
        if y > int(floor.ycor()+40):
            inair == True

    leftwall.goto(player.xcor() - 40, player.ycor())

    if leftwall.distance(minlwtile) < 45:
        player.xV = 0
        player.setx(minlwtile.xcor() + 80)

    rightwall.goto(player.xcor()+40, player.ycor())

    if rightwall.distance(minrwtile) < 45:
        player.xV = 0
        player.setx(minrwtile.xcor() - 80)


def leftmovement():
    player.xV = -10
def leftstop():
    player.xV = 0
def rightmovement():
    player.xV = 10
def rightstop():
    player.xV = 0




def updategame():
    global x, y, inair
    x = player.xcor()
    y = player.ycor()
    player.setpos(x+player.xV,y+player.yV)
    if inair == True:
        player.yV-=1
    collision()
    screen.update()
    screen.ontimer(updategame, 30)

screen.ontimer(updategame, 30)


screen.onkeypress(jump, "Up")
screen.onkeypress(jump, "w")
screen.onkeypress(leftmovement, "Left")
screen.onkeypress(leftmovement, "a")
screen.onkeypress(rightmovement, "Right")
screen.onkeypress(rightmovement, "d")
screen.onkeyrelease(leftstop, "Left")
screen.onkeyrelease(leftstop, "a")
screen.onkeyrelease(rightstop, "Right")
screen.onkeyrelease(rightstop, "d")


screen1 = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]]

jumptiles = []
lwalltiles = []
rwalltiles = []
tiles = []
rendered = []
def render(screen):
    rendererY = 480
    rendererX = -960
    for i in screen:
        rendererY -= 80
        rendererX = -960
        for j in i:
            rendererX += 80
            if j == 1:
                grass = turtle.Turtle()
                grass.penup()
                grass.color("green")
                grass.turtlesize(4)
                grass.shape("square")
                grass.goto(rendererX,rendererY)
                jumptiles.append(grass)
                lwalltiles.append(grass)
                rwalltiles.append(grass)
                tiles.append(grass)










render(screen1)


#measuring sticks
new = turtle.Turtle()
new.shape("square")
new.color("black")
new.turtlesize(4)
new.goto(915,0)
new2 = turtle.Turtle()
new2.shape("square")
new2.color("red")
new2.turtlesize(4)
new2.goto(0,470)


screen.listen()
screen.mainloop()