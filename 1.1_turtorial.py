'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
yoda=turtle.Turtle()
screen=turtle.Screen() # makes a screen object
screen.bgcolor('#0000aa') # colors the screen
yoda.pensize(3) # width of pen line
yoda.speed(10)  # speed of drawing. Go fast to not waste time.
yoda.penup()
yoda.goto(-30,-60)
yoda.pendown()
yoda.end_fill()
yoda.color("orange")
yoda.circle(80)#head
yoda.goto(-180, 0)#rest of the body
yoda.goto(-180, 40)
yoda.goto(-30, 100)
yoda.penup()
yoda.goto(-180, 0)#preparing to make tail
yoda.pendown()
yoda.goto(-220, -40)#tail
yoda.goto(-220,80)
yoda.goto(-180, 40)
yoda.penup()
yoda.goto(-30,100)#preperation to take top fin
yoda.pendown()
yoda.goto(-50, 160)
yoda.penup()
yoda.setpos(200,-300)
yoda.pendown()
yoda.pencolor('#00FF00')


yoda.write('Sign Your Name Here',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
