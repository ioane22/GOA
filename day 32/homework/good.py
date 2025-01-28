from turtle import *

def draw_square(x_cor, y_cor):
    penup()
    goto(x_cor, y_cor)
    pendown()

    
    for i in range(4):
        forward(200)
        left(90)


draw_square(-200, -20)
draw_square(200, -20)
draw_square(-200, -300)
draw_square(200, -300)
exitonclick()