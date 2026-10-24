import pgzrun
import random
WIDTH=819
HEIGHT=819
TITLE="shooter"
Alien=Actor("alien")
message="welcome to shooter"



def draw():
    screen.fill("grey")
    Alien.draw()
    screen.draw.text(message,(0,0))

def alienposition():
    Alien.x=random.randint(0,819)
    Alien.y=random.randint(0,819)
alienposition()

def on_mouse_down(pos):
    global message
    if Alien.collidepoint(pos):
        alienposition() 
        message="good shot"
    else:
        message="you missed"
pgzrun.go()