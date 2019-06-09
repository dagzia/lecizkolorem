def setup():
    frameRate(60)
    rectMode(CENTER)
    size(450,450)
    global kolory
    kolory=((255,0,0),(0,255,0),(0,0,255))
    fill(*kolory[0])
    strokeWeight(5)
    stroke(*kolory[2])
    global x
    global y
    x = 20
    y = 20
    
def draw():
    global x
    x=x+1
    global y
    y=y+1
    rect(x,y, height/4, width/4)
    if x > 400:
        exit()
    global kolory
    if x > 150:
        fill(*kolory[1])
        stroke(*kolory[0])    
    if x > 250:
        fill(*kolory[2])
        stroke(*kolory[1])
    
