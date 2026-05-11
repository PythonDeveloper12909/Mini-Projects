from cmu_graphics import *

import random

index=0

randomindex=random.randint(0,39)

hints={
    'ability':'A skill or talent  somone possesses',
    'about':'Related to or concering something',
    'above':'At a higher position',
    'abroad':'In or to another country',
    'absence':'the state of not being present',
    'absent':'Not present somewhere',
    'absolute':'Complete or total',
    'abstract':'Existing as an idea rather than physically',
    'academic':'Related to education or studies',
    'academy':'A place for learning or training',
    'accent':'A distinctive way of pronouncing words',
    'accept':'to agree to receive or approve',
    'access':'the ability to enter or use something',
    'accident':'An unexpected harmful event',
    'account':'User profile or bank record',
    'accuracy':'The quality of being correct and precise',
    'accurate':'Free from mistakes and very exact',
    'accused':'A person charged with doing something wrong',
    'achieve':'To successfully reach a goal or result',
    'acids':"Used in reactions",
    "python": "Popular coding language",
    "galaxy": "Contains billions of stars",
    "oxygen": "Makes breathing possible",
    "pyramid": "Famous in ancient Egypt",
    "volcano": "Erupts with lava",
    "compass": "Shows north direction",
    "diamond": "Hardest natural substance",
    "library": "Silent reading place",
    "gravity": "Keeps planets in orbit",
    "whisper": "Barely audible speech",
    "journey": "Travel with a destination",
    "tornado": "Spinning funnel storm",
    "keyboard": "Used beside a monitor",
    "penguin": "Bird living in cold regions",
    "battery": "Powers many devices",
    "helmet": "Worn for head safety",
    "planet": "Revolves around the sun",
    "treasure": "Often searched by pirates",
    "desert": "Very little rainfall",
    "lantern": "Old-style portable light"
    }

def onAppStart(app):
    global randomindex
    allwords=list(hints.keys())
    app.randomword=allwords[randomindex]
    app.score=0
    app.input=''
    app.hints=hints[app.randomword]
    app.length=len(app.randomword)
    
def onStep(app):
    global randomindex
    allwords=list(hints.keys())    
    app.randomword=allwords[randomindex]
    app.hints=hints[app.randomword]
    app.length=len(app.randomword)

    
def onKeyPress(app,key):
    global index,gameOver,gameWon,randomindex
    keycheck=len(key)==1 and key.isalpha()
    if app.score<=-7:
        return
    
    if(keycheck):    
        app.input=app.input+key
     
        if(len(app.input)>=len(app.randomword) and app.input==app.randomword):
            randomindex=random.randint(0,39)
            app.input=''
            app.score+=1
        elif(app.input!=app.randomword and len(app.input)>=len(app.randomword)):
            app.score-=1
            randomindex=random.randint(0,39)
            app.input=''
    else:
        if key=='backspace':
            app.input=app.input[:-1]
    
            
def onMousePress(app,mouseX,mouseY):
    global randomindex
    if app.score<=-7:
        
        if 160<=mouseX<=260 and 250<=mouseY<=300:
            app.score=0
            randomindex=random.randint(0,39)
            
    if app.score>=10:
        
        if 160<=mouseX<=260 and 250<=mouseY<=300:
            app.score=0
            randomindex=random.randint(0,39)
        
    
    
def redrawAll(app):
    if app.score<=-7:
        butw=100
        buth=50
        drawLabel('You lost!',200,200,size=30)
        drawRect(160,250,butw,buth,fill='red')
        drawLabel('Restart',160+(butw/2),250+(buth/2),size=20,fill='yellow')
        
    elif app.score>=10:
        butw=100
        buth=50
        drawLabel('You Won!',200,200,size=30)
        drawRect(160,250,butw,buth,fill='red')
        drawLabel('Restart',160+(butw/2),250+(buth/2),size=20,fill='yellow')
        
    else:
        drawLabel(f'Score:{app.score}',40,100,size=20)
        drawLabel('Reach 10 to win the game and -7 to lose the game',200,50,size=17,fill='blue')
        drawLine(150,220,150,100)
        drawLine(150,100,200,100)
        drawLabel('Press key to enter the words',200,250,size=20,fill='red')
        drawLabel(f'Hint: {app.hints}',200,300,size=17)
        drawLabel(f'Length: {app.length}',350,100,size=18)
        x=100
        gap=25
        for i in range(len(app.randomword)):
            drawLine(x,365,x+20,365)
            if i < len(app.input):
                drawLabel(f'{app.input[i]}',x+10,355,size=20)
            x+=gap
        if app.score<=-1:
            drawLine(200,100,200,125)
        if app.score<=-2:
            drawCircle(200,135,10,fill=None,border='black')
        if app.score<=-3:
            drawLine(200,145,200,190)
        if app.score<=-4:
            drawLine(200,145,175,160)
        if app.score<=-5:
            drawLine(200,145,225,160)
        if app.score<=-6:
            drawLine(200,190,175,200)
        if app.score<=-7:
            drawLine(200,190,225,200)
            
        

def main():
    runApp()

main()

