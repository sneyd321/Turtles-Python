import turtle;
import random;
import time;
from tkinter import messagebox

#Create Window
window = turtle.Screen()
#Set backgound colour
window.bgcolor("darkgreen")
#Get screen size of computer
screen = window.screensize()

width = int(window.numinput("Race Track Editor", "Enter the width of the tack in pixels"))
height = int(window.numinput("Race Track Editor", "Enter the height of the tack in pixels"))
speed = int(window.numinput("Race Track Editor", "Enter the max speed the turtles can race"))
lapNumber = int(window.numinput("Race Track Editor", "Enter the number of laps"))
#Create turtle objects           
mcLaren = turtle.Turtle()
ferrari = turtle.Turtle()

def configTurtles():
    """Configure shape and colour of turtles"""
    mcLaren.shape("turtle")
    mcLaren.color("Red")
    ferrari.shape("turtle")
    ferrari.color("Blue")
    mcLaren.penup()
    ferrari.penup()

configTurtles()

#Make an atempt to position turtles correctly on screen
mcLaren.setpos(-(screen[0])/3 - (screen[0]/2), -(screen[1]/3) - (screen[1]/2))
#set starting position for red turtle
startPos1 = mcLaren.pos()
ferrari.penup()
#Make an atempt to position turtles correctly on screen
ferrari.setpos((screen[0])/3, -(screen[1])/3 - (screen[1]/2))
#set starting position for blue turtle
startPos2 = ferrari.pos()
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
#Global variable to keep track of number of laps
redCounter = 0
blueCounter = 0

def raceTurtleForX(distance, turtle, startPos):
    """Make turtle move left to right along X axis""" 
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
    """Make Turtle move from bottom to top along y axis"""
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
    """make turtle move from right to left along x axis"""
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
    """make turtle move from top to bottom along y axis"""
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
    """Function that runs the race"""    
    while (True):  
        #start timer
        startTime = time.time()
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
            
        #if the red car completed a certain number of laps
        if redCounter == lapNumber:
            messagebox.showinfo("Race Track Editor", "Mclaren won the race")
            #end timer
            endTime = time.time()
            messagebox.showinfo("Race Track Editor", "Race time was: " + str(round((endTime - startTime), 2)) + "seconds")
            
        #if the blue car completed a certain number of laps
        if blueCounter == lapNumber:
            messagebox.showinfo("Race Track Editor", "Ferrari won the race")
            #end timer
            endTime = time.time()
            messagebox.showinfo("Race Track Editor", "Race time was: " + str(round((endTime - startTime), 2)) + "seconds")
            
#ask user is they are ready to race, can the feel the excitement
messagebox.showinfo("Race Track Editor", "Ready to Race")

while (True):
    
    #ask user if they would like to race again
    result = messagebox.askyesno("Race Track Editor", "Would you like to race again?")
    #if yes
    if result == True:      
        #resey position
        mcLaren.setpos(-(screen[0])/3 - (screen[0]/2), -(screen[1]/3) - (screen[1]/2))
        ferrari.setpos((screen[0])/3, -(screen[1])/3 - (screen[1]/2))
        #ask user is they are ready to race, can the feel the excitement
        messagebox.showinfo("Race Track Editor", "Ready to Race")
        #lap counter
        redCounter = 0
        blueCounter = 0
        runRace()
    else:
        break
        
window.bye();
    

 
    
    

        





