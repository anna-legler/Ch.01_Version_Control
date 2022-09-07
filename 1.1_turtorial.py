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
yoda.color("orange")
yoda.begin_fill()
yoda.circle(80)#head
yoda.end_fill()
yoda.begin_fill()#body start
yoda.goto(-180, 0)
yoda.goto(-180, 40)
yoda.goto(-30, 100)
yoda.end_fill()#body end
yoda.penup()
yoda.goto(-180, 0)#preparing to make tail
yoda.pendown()
yoda.begin_fill()#tail start
yoda.goto(-220, -40)
yoda.goto(-220,80)
yoda.goto(-180, 40)
yoda.end_fill()#tail end
yoda.penup()
yoda.goto(-30,100)#preperation to take top fin
yoda.pendown()
yoda.begin_fill()#top fin start
yoda.goto(-80, 140)
yoda.goto(-130,140)
yoda.goto(-100,120)
yoda.goto(-110,68)
yoda.end_fill()#top fin end
yoda.penup()
yoda.color("#ff8800")#preparing for side fin
yoda.goto(-40,60)
yoda.pendown()#side fin start
yoda.goto(-100,45)
yoda.goto(-120,-10)
yoda.goto(-90,10)
yoda.goto(-40,0)
yoda.penup()#side fin end
yoda.goto(0,30)#whites of eye preperation
yoda.color("white")
yoda.pendown()#whites of eyes start
yoda.begin_fill()
yoda.circle(20)
yoda.end_fill()
yoda.penup()#whites of eyes end
yoda.goto(0,35)#pupil preperation
yoda.color("black")
yoda.pendown()
yoda.begin_fill()
yoda.circle(15)
yoda.end_fill()
yoda.penup()#pupil end
yoda.goto(8,50)#eye shine preperation
yoda.color("white")
yoda.pendown()#eye shine start
yoda.begin_fill()
yoda.circle(3)
yoda.end_fill()#eyeshine end
yoda.penup()#signature prep
yoda.setpos(200,-300)
yoda.pendown()
yoda.pencolor('white')



yoda.write('Anna Legler',font=("Comic Sans", 16, "normal"))
# signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
