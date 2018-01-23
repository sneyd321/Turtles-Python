import turtle;
import random;
import time;
from tkinter import messagebox

def createDialog(title, description):
    """Create Dialog box to interact with user. Also to validate whether user clicked on the "X" to close the dialogbox. Returns an int value."""
    while True:
        try:
            #Create messagebox and get value from user  
            value = int(window.numinput(title, description))
            #return value
            return value
        #if user clicks on the "X"
        except TypeError:
            #prompt user again 
            continue


def configTurtles():
    """Configure shape and colour of turtles"""
    mcLaren.shape("turtle")
    mcLaren.color("Red")
    ferrari.shape("turtle")
    ferrari.color("Blue")
    mcLaren.penup()
    ferrari.penup()

def drawTrack():
    """Draw the race track for the turtles"""
    mcLaren.pendown()
    ferrari.pendown()
    #draw race track given users dimentions
    for i in range(0, 2):
        mcLaren.forward(width)
        ferrari.forward(width)
        mcLaren.left(90)
        ferrari.left(90)
        mcLaren.forward(height)
        ferrari.forward(height)
        mcLaren.left(90)
        ferrari.left(90)
    #Pen up for cleaner look
    mcLaren.penup()
    ferrari.penup()

def raceTurtleForX(distance, turtle, startPos):
    """Make turtle move left to right along bottom X axis""" 
    #Round start position to avoid working with irrational floating points
    startPosition = round(startPos[0], 4)
    #Round x coordinate to avoid working with irrational floating points
    xPos = round(turtle.xcor(), 4)
    #Round end position to avoid working with irrational floating points
    endPosition = round(startPosition + distance, 4)
    #If the turtle reaches the top right corner execute raceTurtleForX2
    if round(turtle.ycor(), 4) == round(startPos[1] + height, 4):
        raceTurtleForX2(turtle, startPos)
    #otherwise
    else:
        #if the current position is less then the end position move forward
        if xPos < endPosition:
            turtle.forward(random.randint(0, speed))
        #if it is greater then move the turtle to the correct position and turn left
        elif xPos > endPosition:          
            turtle.setx(endPosition)
            turtle.left(90)
    
       
def raceTurtleForY(distance, turtle, startPos):
    """Make Turtle move from bottom to top along right y axis"""
    #Round start position to avoid working with irrational floating points
    startPosition = round(startPos[1], 4)
    #Round end position to avoid working with irrational floating points
    endPosition = round(startPosition + distance, 4)
    #Round y coordinate to avoid working with irrational floating points
    yPos = round(turtle.ycor(), 4)
    
    #If the turtle reaches the top right corner execute raceTurtleForY2
    if round(turtle.xcor(), 4) == round(startPos[0], 4):
        raceTurtleForY2(turtle, startPos)
    else:
        #if the current position is less then the end position move forward
        if yPos < endPosition:           
            turtle.forward(random.randint(0, speed))
        #if it is greater then move the turtle to the correct position and turn left
        elif yPos > endPosition:
            turtle.sety(endPosition)
            turtle.left(90)
            
    

def raceTurtleForX2(turtle, startPos):
    """make turtle move from right to left along top x axis"""
    #Round end position to avoid working with irrational floating points
    endPosition = round(startPos[0], 4)
    #Round x coordinate to avoid working with irrational floating points
    xPos = round(turtle.xcor(), 4)
    #if the current position is less then the end position move forward
    if xPos > endPosition:         
        turtle.forward(random.randint(0, speed))
    #if it is greater then move the turtle to the correct position and turn left
    elif xPos < endPosition:
        turtle.setx(startPos[0])
        turtle.left(90)

def raceTurtleForY2(turtle, startPos):
    """make turtle move from top to bottom along left y axis"""
    #Round end position to avoid working with irrational floating points
    endPosition = round(startPos[1], 4)
    #Round y coordinate to avoid working with irrational floating points
    yPos = round(turtle.ycor(), 4)
    #if the current position is less then the end position move forward
    if yPos > endPosition:         
        turtle.forward(random.randint(0, speed))
    #if it is greater then move the turtle to the correct position and turn left
    elif yPos < endPosition:
        turtle.sety(endPosition)
        turtle.left(90)
        #if red turtle completes lap
        if turtle.color() == ("Red", "Red"):
            #get global variable redCounter 
            global redCounter 
            #record lap count
            redCounter += 1
        #if blue turtle completes lap
        if turtle.color() == ("Blue", "Blue"):
            #get global variable blueCounter 
            global blueCounter
            #record lap count
            blueCounter +=1

def runRace(): 
    """Function that runs the race and determines winner"""   
    #start timer
    startTime = time.time()
    while (True):          
        #execute running race along x axis one turtle at a time
        raceTurtleForX(width, mcLaren, startPos1)   
        raceTurtleForX(width, ferrari, startPos2)           
        #execute running race along y axis one turtle at a time
        raceTurtleForY(height, mcLaren, startPos1)
        raceTurtleForY(height, ferrari, startPos2)
        #if there was a tie
        if redCounter == lapNumber and blueCounter == lapNumber:
            messagebox.showinfo("Race Track Editor", "There was a Tie")
            #end timer
            endTime = time.time()
            break;          
        #if the red car completed a certain number of laps
        if redCounter == lapNumber:
            messagebox.showinfo("Race Track Editor", "Mclaren won the race")
            #end timer
            endTime = time.time()
            messagebox.showinfo("Race Track Editor", "Race time was: " + str(round((endTime - startTime), 2)) + " seconds")
            break;
        #if the blue car completed a certain number of laps
        if blueCounter == lapNumber:
            messagebox.showinfo("Race Track Editor", "Ferrari won the race")
            #end timer
            endTime = time.time()
            messagebox.showinfo("Race Track Editor", "Race time was: " + str(round((endTime - startTime), 2)) + " seconds")
            break;

def run():
    """Prompts user if they would like to race again and starts the race"""
    #Draw the track
    drawTrack()
    #Ask user if they want to race again
    while (True):
        #ask user if they would like to race again
        result = messagebox.askyesno("Race Track Editor", "Ready to Race!")
        #if yes
        if result == True:      
            #reset position
            mcLaren.setpos(-(screen[0])/3 - (screen[0]/2), -(screen[1]/3) - (screen[1]/2))
            mcLaren.setheading(0)
            ferrari.setpos((screen[0])/3, -(screen[1])/3 - (screen[1]/2))
            ferrari.setheading(0)
            #lap counter
            global redCounter 
            redCounter = 0
            global blueCounter 
            blueCounter = 0
            runRace()
        else:
            break

"""Global Variable and Initalization"""
#Create Window
window = turtle.Screen()
#Set backgound colour
window.bgcolor("darkgreen")
#Get screen size of computer
screen = window.screensize()

#Get data from user
width = createDialog("Race Track Editor", "Enter the width of the tack in pixels")
height = createDialog("Race Track Editor", "Enter the height of the tack in pixels")
speed = createDialog("Race Track Editor", "Enter the max speed turtles can race")
lapNumber = createDialog("Race Track Editor", "Enter the the number of laps")
        
#Create turtle objects           
mcLaren = turtle.Turtle()
ferrari = turtle.Turtle()

#Configure turtles
configTurtles()

#Give cleaner look to race track
mcLaren.penup()
#Make an atempt to position turtles correctly on screen
mcLaren.setpos(-(screen[0])/3 - (screen[0]/2), -(screen[1]/3) - (screen[1]/2))
#set global variable that holds starting position for red turtle
startPos1 = mcLaren.pos()

#Give cleaner look to race track
ferrari.penup()
#Make an atempt to position turtles correctly on screen
ferrari.setpos((screen[0])/3, -(screen[1])/3 - (screen[1]/2))
#set global variable that holds starting position for blue turtle
startPos2 = ferrari.pos()

#Global variable to keep track of number of laps
redCounter = 0
blueCounter = 0

run()

window.bye();
    

 
    
    

        





