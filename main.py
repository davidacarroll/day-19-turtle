from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

bet_ok = False
while not bet_ok:
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?Enter a color (red, orange, yellow, green, blue, purple): ")
    if user_bet in colors:
        print(f"{user_bet} is an acceptable bet")
        bet_ok = True
    else:
        print(f"{user_bet} not an acceptable bet. Try again")

y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []

for turtle_index in range(0, len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.speed("slow")
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

winner = "black"

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        #print(f"Turtle color is {turtle.fillcolor()}, type is {type(turtle.fillcolor())}")
        turtle.goto(x=turtle.xcor() + random_distance, y=turtle.ycor())
        if turtle.xcor() >= 230:
            winner = turtle.fillcolor()
            is_race_on = False

if user_bet == winner:
    print(f"You Win!!! The winner is {winner}")
else:
    print(f"You Lose!!! The winner is {winner}")
screen.exitonclick()


# def move_forward():
#     titus.forward(10)
#
# def move_backward():
#     titus.backward(10)
#
# def move_clockwise():
#     titus.right(10)
#
# def move_counterclockwise():
#     titus.left(10)
#
# def clear():
#     titus.clear()
#     titus.penup()
#     titus.goto(0,0)
#     titus.pendown()
#
# def etch():
#     screen.listen()
#     screen.onkey(key="f", fun=move_forward)
#     screen.onkey(key="a", fun=move_backward)
#     screen.onkey(key="d", fun=move_clockwise)
#     screen.onkey(key="s", fun=move_counterclockwise)
#     screen.onkey(key="c", fun=clear)
