import turtle
import pandas
screen=turtle.Screen()

screen.title("U.S.States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states=[]
#this function gives us the x and y co-ordinates of the point we click using mouse
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor())
# turtle.mainloop()
# this is to make the screen remain as exit on click makes the screen disspear

data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()


while len(guessed_states)<50:
    answer_state = screen.textinput(f"{len(guessed_states)}/ 50 correct states", "what's another state name?").title()
    print(answer_state)
    if answer_state=="Exit":
        missing_states=[name for name in all_states if (name not in guessed_states)]
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("a.csv")

        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)
        #or i can use
    # state_data.state.item() in place of answer state
