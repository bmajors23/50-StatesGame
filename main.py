import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guess_number = 1
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

turtle = turtle.Turtle()
turtle.hideturtle()
turtle.penup()

while guess_number <= 50:
    answer_state = screen.textinput(title=f"Guess the State. ({guess_number}/50)", prompt="What's another state's name?")
    if answer_state.title() in all_states:
        state_row = data[data.state == answer_state.title()]
        x = int(state_row.x)
        y = int(state_row.y)
        coordinates = (x, y)
        turtle.goto(coordinates)
        turtle.pendown()
        turtle.write(answer_state.title(), True, align="center")
        turtle.penup()
        guess_number += 1
    else:
        pass

turtle.goto(0, 0)
turtle.pendown()
turtle.write("You win!", True, align="center")

screen.exitonclick()



