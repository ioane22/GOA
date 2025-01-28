from turtle import *

# პირველი კვადრატი
penup()
goto(100,100)
pendown()

forward(200)
for i in range(3):
    left(90)
    forward(200)

# მეორე კვადრტი
penup()
goto(-100,100)
pendown()

left(90)

for i in range(4):
    left(90)
    forward(200)

# მესამე კვადრატი
penup()
goto(-100,-300)
pendown()

for i in range(4):
    left(90)
    forward(200)
 
# მეოთხე კვადრატი
penup()
goto(300, -300)
pendown()

for i in range(4):
    left(90)
    forward(200)


exitonclick()