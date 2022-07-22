import turtle
import time
import random
import math
import itertools
import tkinter
import os
import atexit

def shutthehellup():
    os.system("pkill aplay")

os.system("aplay bgm.wav &")
atexit.register(shutthehellup)

screen = turtle.Screen()
screen.tracer(0)
screen.title("Platforming")
screen.setup(width=1880, height=980)
screen.bgpic("SWBG.gif")

screen.addshape("Grass.gif")
screen.addshape("Dirt.gif")
screen.addshape("Mosquito.gif")
screen.addshape("spikes.gif")
screen.addshape("Mosquitof.gif")
screen.addshape("Bogbeast.gif")
screen.addshape("Bogbeastf.gif")
screen.addshape("BogbeastIdle.gif")
screen.addshape("BogbeastIdleF.gif")
screen.addshape("BogbeastJump.gif")
screen.addshape("BogbeastJumpF.gif")
screen.addshape("saw1.gif")
screen.addshape("saw2.gif")
screen.addshape("saw3.gif")
screen.addshape("saw4.gif")
screen.addshape("BottomAcid.gif")
screen.addshape("TopAcid.gif")
screen.addshape("DangerSign.gif")
screen.addshape("Endscreen.gif")
screen.addshape("Meat.gif")


player = turtle.Turtle()
player.shape("Bogbeast.gif")
player.penup()
player.turtlesize(4)
player.goto(-780,-330)
player.yV = 0
player.xV = 0
player.Forward = True
x = player.xcor()
y = player.ycor()

floor = turtle.Turtle()
floor.hideturtle()
floor.shape("square")
floor.color("black")
floor.penup()
floor.goto(0,0)

leftwall = turtle.Turtle()
leftwall.hideturtle()
leftwall.shape("square")
leftwall.color("red")
leftwall.penup()
leftwall.goto(0,0)

rightwall = turtle.Turtle()
rightwall.hideturtle()
rightwall.shape("square")
rightwall.color("yellow")
rightwall.penup()
rightwall.goto(0,0)

bordrawer = turtle.Turtle()
bordrawer.penup()
bordrawer.goto(-960,480)
bordrawer.pensize(80)
bordrawer.pendown()
bordrawer.goto(-960,-480)
bordrawer.goto(961,-480)
bordrawer.goto(961,480)
bordrawer.goto(-960,480)

player.spawnx = -780
player.spawny = -330

inair = True
Jumps = 0
cscreen = ""

def jump():
    global Jumps, inair
    if Jumps < 2:
        inair = True
        player.yV = +13
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
        if y < int(floor.ycor()+40) and y > int(floor.ycor()):
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
    player.Forward = False
def leftstop():
    player.xV = 0
def rightmovement():
    player.xV = 10
    player.Forward = True
def rightstop():
    player.xV = 0

def Rscreenswitch(screen):
    global x, cscreen, tiles, y
    x = player.xcor()
    if screen == screen1:
        if x > 960:
            derender(tiles)
            render(screen2)
            cscreen = screen2
            player.setx(-1*x+80)
            x = player.xcor()
            y = player.ycor()
            player.spawnx = -880
            player.spawny = -240
    if screen == screen2:
        if x > 960:
            derender(tiles)
            render(screen3)
            cscreen = screen3
            player.setx(-1*x+80)
            x = player.xcor()
            y = player.ycor()
            player.spawnx = -880
            player.spawny = -240
    if screen == screen3:
        if x > 960:
            derender(tiles)
            render(screen4)
            cscreen = screen4
            player.setx(-1*x+80)
            x = player.xcor()
            y = player.ycor()
            player.spawnx = -880
            player.spawny = -240
    if screen == screen4:
        if x > 960:
            derender(tiles)
            render(screen5)
            cscreen = screen5
            player.setx(-1*x+80)
            x = player.xcor()
            y = player.ycor()
            player.spawnx = -880
            player.spawny = -240
    if screen == screen5:
        if x > 960:
            derender(tiles)
            render(screen6)
            cscreen = screen6
            player.setx(-1*x+80)
            x = player.xcor()
            y = player.ycor()
            player.spawnx = -880
            player.spawny = -240
    if screen == screen6:
        if x > 610:
            screen.clear()
            bordrawer = turtle.Turtle()
            bordrawer.penup()
            bordrawer.goto(-960, 480)
            bordrawer.pensize(80)
            bordrawer.pendown()
            bordrawer.goto(-960, -480)
            bordrawer.goto(961, -480)
            bordrawer.goto(961, 480)
            bordrawer.goto(-960, 480)
            screen.bgpic("Endscreen.gif")


def Lscreenswitch(screen):
    global x, cscreen, tiles
    x = player.xcor()
    if screen == screen2:
        if x < -960:
            derender(tiles)
            render(screen1)
            cscreen = screen1
            player.setx(-1*x-80)
            player.spawnx = 880
            player.spawny = 240
    if screen == screen3:
        if x < -960:
            derender(tiles)
            render(screen2)
            cscreen = screen2
            player.setx(-1*x-80)
            player.spawnx = 880
            player.spawny = 240
    if screen == screen4:
        if x < -960:
            derender(tiles)
            render(screen3)
            cscreen = screen3
            player.setx(-1*x+80)
            x = player.xcor()
            y = player.ycor()
            player.spawnx = 880
            player.spawny = 240
    if screen == screen5:
        if x > 960:
            derender(tiles)
            render(screen4)
            cscreen = screen4
            player.setx(-1*x+80)
            x = player.xcor()
            y = player.ycor()
            player.spawnx = 880
            player.spawny = 240
    if screen == screen6:
        if x > 960:
            derender(tiles)
            render(screen5)
            cscreen = screen5
            player.setx(-1*x+80)
            x = player.xcor()
            y = player.ycor()
            player.spawnx = 880
            player.spawny = 240

def die():
    global deathtiles
    for i in deathtiles:
        if player.distance(i) < 60:
            derender(tiles)
            derender(deathtiles)
            render(cscreen)
            player.goto(player.spawnx,player.spawny)
            player.xV = 0
            player.yV = 0
    diefall()

def diefall():
    if player.ycor() < -560:
        derender(tiles)
        derender(deathtiles)
        render(cscreen)
        player.xV = 0
        player.yV = 0
        player.goto(player.spawnx,player.spawny)

def sawfall():
    for i in failltiles:
        if player.ycor() < i.ycor():
            if i.xcor() - 40 < player.xcor() < i.xcor() + 40:
                i.yV = -60
        i.sety(i.ycor()+i.yV)

def lrmove():
    for i in mosquitoms:
        for j in mostiles:
            if i.distance(j) < 80:
                i.xV = -1 * i.xV
            if i.xV < 0:
                i.shape("Mosquitof.gif")
            else:
                i.shape("Mosquito.gif")
        i.setx(i.xcor()+i.xV)



def anim():
    global sawcount
    if player.Forward == True:
        if player.xV == 0:
            if player.yV == 0:
                player.shape("BogbeastIdle.gif")
            if player.yV >= 1:
                player.shape("BogbeastJump.gif")
        else:
            player.shape("Bogbeast.gif")
    elif player.Forward == False:
        if player.xV == 0:
            if player.yV == 0:
                player.shape("BogbeastIdleF.gif")
            if player.yV >= 1:
                player.shape("BogbeastJumpF.gif")
        else:
            player.shape("Bogbeastf.gif")

def updategame():
    global x, y, inair, cscreen
    x = player.xcor()
    y = player.ycor()
    player.setpos(x+player.xV,y+player.yV)
    if inair == True:
        player.yV-=1
    collision()
    die()
    sawfall()
    lrmove()
    anim()
    Rscreenswitch(cscreen)
    Lscreenswitch(cscreen)
    print(player.pos())
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

a = 10
b = 11

screen1 = [
[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

screen2 = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,0,0,a,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,2,2,8,8,8,8,8,1,1,1,1,1,1,1,1,1]]

screen3 = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,1,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7],
[0,0,0,0,0,2,2,0,0,0,0,0,0,6,0,0,0,0,0,0,0,0,7],
[1,1,1,1,1,2,2,8,8,8,8,8,8,1,1,1,1,1,1,1,1,1,1]]

screen4 = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[7,0,0,0,0,0,0,0,0,0,0,0,0,0,6,0,0,0,0,0,0,0,7],
[0,0,0,0,0,1,8,8,8,8,8,1,8,8,8,8,8,1,8,8,8,8,8],
[0,0,0,1,1,2,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
[1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

screen5 = [
[0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
[0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,4,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,2,2,8,8,8,8,8,1,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,2,1,1,1,1,1,1,1]]

screen6 = [
[0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,0,0,0,2,0,0,0,0,0,0,0,0,0,0,6,0,0,0,b,0,0,7],
[0,0,0,1,2,8,8,8,8,8,1,8,8,8,8,1,1,1,1,1,1,1,1],
[0,0,0,0,2,9,9,9,9,9,9,9,9,9,9,2,9,9,9,9,9,9,9],
[1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2]]

jumptiles = []
lwalltiles = []
rwalltiles = []
tiles = []
rendered = []
deathtiles = []
failltiles = []
mosquitos = []
mosquitoms = []
mostiles = []
meat = []

"""
1) Grass
2) Dirt
3) Spikes
4) Sawfall
5) Mosquito
6) Mosquitom
7) Top Acid
8) Bottom Acid
a) Sign
"""

def render(screen):
    global cscreen
    rendererY = 480
    rendererX = -960
    cscreen = screen
    for i in screen:
        rendererY -= 80
        rendererX = -960
        for j in i:
            rendererX += 80
            if j == 1:
                grass = turtle.Turtle()
                grass.penup()
                grass.turtlesize(4)
                grass.shape("Grass.gif")
                grass.goto(rendererX,rendererY)
                jumptiles.append(grass)
                lwalltiles.append(grass)
                rwalltiles.append(grass)
                tiles.append(grass)
                mostiles.append(grass)
            if j == 2:
                dirt = turtle.Turtle()
                dirt.penup()
                dirt.turtlesize(4)
                dirt.shape("Dirt.gif")
                dirt.goto(rendererX, rendererY)
                tiles.append(dirt)
                jumptiles.append(dirt)
                lwalltiles.append(dirt)
                rwalltiles.append(dirt)
                mostiles.append(dirt)
            if j == 3:
                saw = turtle.Turtle()
                saw.penup()
                saw.turtlesize(4)
                saw.shape("spikes.gif")
                saw.goto(rendererX, rendererY)
                tiles.append(saw)
                deathtiles.append(saw)
            if j == 4:
                sawfall = turtle.Turtle()
                sawfall.penup()
                sawfall.turtlesize(4)
                sawfall.shape("saw1.gif")
                sawfall.goto(rendererX, rendererY)
                sawfall.yV = 0
                sawfall.Count = 0
                tiles.append(sawfall)
                deathtiles.append(sawfall)
                failltiles.append(sawfall)
            if j == 5:
                mosquito = turtle.Turtle()
                mosquito.penup()
                mosquito.turtlesize(4)
                mosquito.shape("Mosquito.gif")
                mosquito.goto(rendererX, rendererY)
                mosquito.xV = 0
                tiles.append(mosquito)
                deathtiles.append(mosquito)
                mosquitos.append(mosquito)
            if j == 6:
                mosquitom = turtle.Turtle()
                mosquitom.penup()
                mosquitom.turtlesize(4)
                mosquitom.shape("Mosquito.gif")
                mosquitom.goto(rendererX, rendererY)
                mosquitom.xV = -10
                mosquitoms.append(mosquitom)
                deathtiles.append(mosquitom)
                tiles.append(mosquitom)
            if j == 7:
                invisible = turtle.Turtle()
                invisible.penup()
                invisible.hideturtle()
                invisible.turtlesize(4)
                invisible.goto(rendererX, rendererY)
                mostiles.append(invisible)
                tiles.append(invisible)
            if j == 8:
                acid = turtle.Turtle()
                acid.penup()
                acid.shape("TopAcid.gif")
                acid.turtlesize(4)
                acid.goto(rendererX,rendererY)
                tiles.append(acid)
                deathtiles.append(acid)
            if j == 9:
                acidb = turtle.Turtle()
                acidb.penup()
                acidb.shape("BottomAcid.gif")
                acidb.turtlesize(4)
                acidb.goto(rendererX,rendererY)
                tiles.append(acidb)
                deathtiles.append(acidb)
            if j == a:
                sign = turtle.Turtle()
                sign.penup()
                sign.shape("DangerSign.gif")
                sign.turtlesize(4)
                sign.goto(rendererX,rendererY-30)
                tiles.append(sign)
            if j == b:
                meatt = turtle.Turtle()
                meatt.penup()
                meatt.shape("Meat.gif")
                meatt.turtlesize(4)
                meatt.goto(rendererX,rendererY)
                tiles.append(meat)
                meat.append(meat)


def derender(tlist):
    for i in tlist:
        i.reset()
        i.penup()
        i.goto(6942,6942)

render(screen1)

"""
measuring sticks
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
"""

screen.listen()
screen.mainloop()