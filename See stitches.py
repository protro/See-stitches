import pgzrun
TITLE='See stitches'
score=0
needles = []
newNeedle = Actor('needle',anchor=(170+50,0))
newNeedle.x = 220
newNeedle.y = 300
needles.append(newNeedle)
needlespeed=2
def draw():
    screen.fill('white')
    for needle in needles:
        needle.draw()
    screen.draw.filled_circle((400,300),80,'blue')
    screen.draw.text(str(score),(50,250),fontsize=50,color='red')
    if needlespeed == 0:
        screen.draw.text('game over',(10,320),fontsize=35,color='red')

def update():
    for needle in needles:
        if needle.x == 400:                   
            needle.angle += needlespeed

def on_mouse_down():
    global newNeedle
    global needlespeed
    global score
    newNeedle = Actor('needle',anchor=(170+50,0))
    newNeedle.x = 400
    newNeedle.y = 300
    if needlespeed > 0:
        score+=1
    for needle in needles:
        if newNeedle.colliderect(needle):
            print('loose')
            needlespeed = 0
            

    needles.append(newNeedle)

pgzrun.go()
