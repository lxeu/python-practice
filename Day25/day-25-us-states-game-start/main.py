import turtle
import pandas

data = pandas.read_csv("day-25-us-states-game-start/50_states.csv")
states = data.state.to_list()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 correct",prompt="Name a state:").title()

    if answer_state == "Exit":
        missing_states = []
        for state in states:
            if answer_state in states and answer_state not in guessed_states:
                missing_states.append(state)
        missing_states_data = pandas.DataFrame(missing_states)
        missing_states_data.to_csv("day-25-us-states-game-start/missed_states.csv")

        break

    for state in states:
        if answer_state == state:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(state_data.x.item(), state_data.y.item())
            t.write(answer_state)