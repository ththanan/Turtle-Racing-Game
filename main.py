from turtle import Turtle, Screen
import random

race_on = True
screen = Screen()
screen.title("Turtle Racing Game")
screen.setup(width=600, height=400)
screen.bgcolor("#8cba9c")

race = Turtle("square")
race.penup()
race.color("#E9E6BF")
race.shapesize(stretch_wid=14, stretch_len=40)


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100, -60, -20, 20, 60, 100]
all_turtles = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-270, y=y_position[turtle_index])
    all_turtles.append(new_turtle)


user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

gameover = Turtle()
gameover.penup()
gameover.hideturtle()
gameover.color("#df6464")
FONT = ("Courier", 12, "normal")

while race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 265:
            race_on = False
            winning = turtle.pencolor()
            if winning == user_bet:
                gameover.write(f"You win!", align="center", font=FONT)
                print(f"You've won! The {winning} turtle is the winner!")
            else:
                gameover.write(f"You lose!", align="center", font=FONT)
                print(f"You've lost! The {winning} turtle is the winner!")



        distance = random.randint(0, 10)
        turtle.forward(distance)


screen.exitonclick()