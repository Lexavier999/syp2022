import turtle
import time
import random

screen = turtle.Screen()
screen.tracer(0)
screen.title("Platforming")
screen.setup(width=1200, height=800)

player = turtle.Turtle()
player.shape("square")
player.color("green")
player.penup()
player.goto(0,0)
player.yV = 0
player.xV = 0
x = player.xcor()
y = player.ycor()

inair = True
Jumps = 0
flags = [False, False]
# Jump Move

def gravity():
    global inair, Jumps, y
    y = player.ycor()
    if inair == True:
        player.yV-=1
    if inair == False:
        player.yV = 0
    player.sety(y+player.yV)

def movement(direction):
    global x, flags
    flags[1] = True
    x = player.xcor()
    if direction == "Left":
        player.xV = -10
    if direction == "Right":
        player.xV = 10
player.setx(x+player.xV)
player.xV=0



def voidfloor():
    global inair, Jumps
    if player.ycor() < -320:
        inair = False
        player.sety(-320)
        Jumps = 0

def jump():
    global inair, Jumps, flags
    if Jumps < 2:
        player.yV = 15
        inair= True
        Jumps+=1
    if Jumps == 2:
        flags[0] = False



def gameupdate():
    global flags
    for i in flags:
        flags[i] = False
    screen.update()
    if flags[0] == False:
        screen.onkeypress(lambda: jump(), "Up")
        screen.onkeypress(lambda: jump(), "w")
    if flags[1] == False:
        screen.onkeypress(lambda: movement("Left"), "Left")
        screen.onkeypress(lambda: movement("Left"), "a")
        screen.onkeypress(lambda: movement("Right"), "Right")
        screen.onkeypress(lambda: movement("Right"), "d")
        print(flags[1])


screen.listen()

while True:
    gravity()
    voidfloor()
    screen.update()
    time.sleep(0.03)
    gameupdate()

screen.mainloop()
