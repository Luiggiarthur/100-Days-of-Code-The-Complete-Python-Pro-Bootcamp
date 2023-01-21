import turtle
import pandas as pd

screen = turtle.Screen()
screen_country = turtle.Turtle()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pd.read_csv("50_states.csv")
df = pd.DataFrame(data)

countries = df["state"].values.tolist()

position_x = df["x"].values.tolist()
position_y = df["y"].values.tolist()
guessed_state = []
score = 0
while score != 50:

    if score > 49:
        screen_country.goto(0, 0)
        screen_country.write("You win!", align="center", font=("Courier", 24, "normal"))
    elif score == 0:
        answer_state = screen.textinput(title="Guess the State", prompt="What's a state's name").title()
    else:
        answer_state = screen.textinput(title=f"{score}/50 States correct",
                                        prompt="What's another state's name").title()
    if answer_state == "Exit":
        missing_states = []
        for state in countries:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn")

        break
    for country in countries:
        if country == answer_state:
            guessed_state.append(answer_state)
            index = countries.index(country)
            screen_country.penup()
            screen_country.hideturtle()
            screen_country.goto(position_x[index], position_y[index])
            screen_country.write(country)
            score += 1


#screen.exitonclick()