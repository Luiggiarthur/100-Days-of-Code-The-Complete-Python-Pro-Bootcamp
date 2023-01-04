from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y = 180
turtle_list = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    y = y - 50
    new_turtle.goto(-240, y)
    turtle_list.append(new_turtle)


is_bet_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? choose your color.").lower()
for item in colors:
    if user_bet == item:
        is_bet_on = True

while is_bet_on:

    for turtle in turtle_list:
        if turtle.xcor() < 230:
            turtle.forward(random.randint(1, 10))
        else:
            is_bet_on = False
            print(f"The winner is the {colors[turtle_list.index(turtle)]} turtle.")
            if colors[turtle_list.index(turtle)] == user_bet:
                print("You won!")
            else:
                print("You lose :(")


screen.exitonclick()
