from turtle import Turtle, Screen
import random

tiny = Turtle()
screen = Screen()
screen.colormode(255)

tiny.speed("fastest")


def get_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, green, blue


def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tiny.pencolor(get_color())
        tiny.circle(100)
        tiny.setheading(tiny.heading() + size_of_gap)


draw_spirograph(10)

screen.exitonclick()
