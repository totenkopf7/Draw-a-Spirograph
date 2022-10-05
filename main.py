import turtle as t
import random


tim = t.Turtle()
tim.shape("turtle")
tim.color("red")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):

        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)


# for i in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# added 90 each time for turning 90 degrees
# directions = [0, 90, 180, 270]
# tim.pensize(7)
# tim.speed("fastest")
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return  random_color
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for draw_side_n in range(3, 11):
#     tim.color(random_color())
#     draw_shape(draw_side_n)
#
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(25)
#     # tim.right(random.choice(directions))
#
#     # set where to head
#     tim.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()
