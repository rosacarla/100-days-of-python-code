# Tartaruga na tela - versão atualizada
import random
import turtle

def isInScreen(wn, t):
    left_bound = -wn.window_width() / 2
    right_bound = wn.window_width() / 2
    top_bound = wn.window_height() / 2
    bottom_bound = -wn.window_height() / 2

    turtle_x = t.xcor()
    turtle_y = t.ycor()

    return left_bound < turtle_x < right_bound and bottom_bound < turtle_y < top_bound

t = turtle.Turtle()
wn = turtle.Screen()

t.shape('turtle')
while isInScreen(wn, t):
    coin = random.randrange(0, 2)
    if coin == 0:
        t.left(90)
    else:
        t.right(90)

    t.forward(50)

wn.exitonclick()
