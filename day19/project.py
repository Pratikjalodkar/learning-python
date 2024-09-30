from turtle import Turtle,Screen
import random


is_race_on = False

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter the color:")
colors = ["red", "orange", "yellow" ,  "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtle = []
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230,y=y_positions[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtle:
        turtle.forward(random.randint(0,10))
    if turtle.xcor() > 230:
        is_race_on = False
        winning_color=turtle.pencolor()
        if winning_color == user_bet:
            print(f"{winning_color} win the race. ")
        else:
            print(f"{user_bet} lost the race. ")



#
# tom = Turtle(shape="turtle")
# tom.penup()
# tom.color(colors[1])
# tom.goto(x=-230,y=-60)
#
# tum = Turtle(shape="turtle")
# tum.penup()
# tum.color(colors[2])
# tum.goto(x=-230,y=-20)
#
# tam = Turtle(shape="turtle")
# tam.penup()
# tam.color(colors[3])
# tam.goto(x=-230,y=20)
#
# tem = Turtle(shape="turtle")
# tem.penup()
# tem.color(colors[4])
# tem.goto(x=-230,y=60)
#
# toom = Turtle(shape="turtle")
# toom.penup()
# toom.color(colors[5])
# toom.goto(x=-230,y=100)


screen.exitonclick()
