import turtle

sally = turtle.Turtle()
sally.color('red')
sally.shape('turtle')
sally.shapesize(1)
sally.speed(2)


def make_shape(distance, angle):
    sally.forward(distance)
    sally.right(angle)


def make_shape_left(distance, angle):
    sally.forward(distance)
    sally.left(angle)


def square_moving(direction):
    if direction == 'fwd right':
        make_shape(100, 90)
        # make_shape(100, 90)
        # make_shape(100, 90)
        # make_shape(100, 90)
    elif direction == 'fwd left':
        make_shape_left(100, 90)
        # make_shape_left(100, 90)
        # make_shape_left(100, 90)
        # make_shape_left(100, 90)


square_moving('fwd right')
square_moving('fwd left')
# print(sally)
my_screen = turtle.Screen()
print(my_screen.canvheight)
turtle.exitonclick()
