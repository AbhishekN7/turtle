import turtle
import time
import random

WIDTH,HEIGHT = 800,800
COLORS=['Red','Green','Blue','Orange','Yellow','Black','Purple','Black','Brown','Cyan']

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter The Number of Racers you want to race : ")
        if racers.isdigit():
            racers=int(racers)
        else:
            print('Input is not Numeric....Try Again!')
            continue
        
        if 2<= racers <=10:
            return racers
        else:
            print('Enter Valid Number (2-10)!')
            
def race(colors):
    turtles = create_turtles(colors)
    
    while True:
        for racer in turtles:
            distance=random.randrange(1,20)
            racer.forward(distance)
        x,y=racer.pos()
        if y>=HEIGHT//2 - 10:
            return colors[turtles.index(racer)]
            

def create_turtles(colors):
    turtles = []
    spacingx=WIDTH//(len(colors)+1)
    for i,color in enumerate(colors):
        racer=turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1) * spacingx, -HEIGHT//2+20)
        racer.pendown()
        turtles.append(racer)
    return turtles
    
    
            
def init_turtle():
    screen=turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Hey Look The Turtle's are Racing!")
    

racers= get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors=COLORS[:racers]

winner = race(colors)
print("The Winner of the Race is color: ",winner)
time.sleep(5)

            
        
        
            
