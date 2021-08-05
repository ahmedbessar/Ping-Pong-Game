# Importing turtle module
import turtle

screen = turtle.Screen() # initialize screen
screen.title("Ping Pong By Bessar") # set the title on the window   
screen.bgcolor("black") # set the background color of the window
screen.setup(width=800, height=600) # set thr width and the height of the window
screen.tracer(0) # Stop the window from updating automatically

#madrab1
madrab1 = turtle.Turtle() #initializes turtle object(shape)
madrab1.speed(0) #set the speed of the animation
madrab1.shape("square") #set the shape of the object
madrab1.color("blue") #set the color of the shape
madrab1.shapesize(stretch_wid=5, stretch_len=1) #stretches the shape to meet the size
madrab1.penup() # no drawing when moving.
madrab1.goto(-350,0) #set the position of the object
#madrab2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=5, stretch_len= 1)
madrab2.penup()
madrab2.goto(350, 0)
#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

#score
score1 =0
score2 =0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.goto(0, 260)
score.write("Player1 = 0 - Player2 : 0", align="center", font = ("Courier",24,"normal"))

#functions
def madrab1_up():
    y = madrab1.ycor() #get the y  coordinate of madrab1
    y += 20 #set y increase by 20
    madrab1.sety(y) #set y of madrab1 to the new y coordinate

def madrab1_down():
    y = madrab1.ycor() #get the y  coordinate of madrab1
    y -= 20 #set y decrease by 20
    madrab1.sety(y) #set y of madrab1 to the new y coordinate

def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)

def madrab2_down():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)

#keyboard bindings
screen.listen() #tell the screen to expect keyboard input
screen.onkeypress(madrab1_up,"w") #when pressing w the function madrab1_up is invoked
screen.onkeypress(madrab1_down, "s") #when pressing s the function madrab1_down is invoked
screen.onkeypress(madrab2_up, "o")
screen.onkeypress(madrab2_down, "k")

#main game loop
while True:
    screen.update() #update the screen while the loop run

    #move ball
    ball.sety(ball.ycor() + ball.dy) #ball starts at 0 and everytime loops run ---> +2 x.axis 
    ball.setx(ball.xcor() + ball.dx) #ball starts at 0 and everytime loops run ---> +2 y.axis

    #border check , top border +300px, bottom border -300px, ball is 20px
    if ball.ycor() > 290: #if the ball is at top border
        ball.sety(290) #set y coordinate +290
        ball.dy *= -1 #reverse direction, making +0.2 ---> -0.2

    if ball.ycor() < -290:  #if the ball is at bottom border
        ball.sety(-290) #set y coordinate -290
        ball.dy *= -1 #reverse direction, making +0.2 ---> -0.2

    if ball.xcor() > 390: #if the ball is at right border
        ball.goto(0,0) #return ball to center
        ball.dx *= -1 #reverse the x direction
        score1 += 1
        score.clear()
        score.write("Player1 = {} - Player2 : {}".format(score1,score2), align="center", font = ("Courier",24,"normal"))

    if ball.xcor() < -390:  
        ball.goto(0,0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player1 = {} - Player2 : {}".format(score1,score2), align="center", font = ("Courier",24,"normal"))
        
    #tsadom madrab and ball 
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1