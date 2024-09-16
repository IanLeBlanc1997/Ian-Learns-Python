import turtle
import pandas
screen = turtle.Screen()
screen.title("US States Game")
screen.bgpic("day_25_reading_CSV_files/US_States_Quiz/blank_states_img.gif")
data = pandas.read_csv("day_25_reading_CSV_files/US_States_Quiz/50_states.csv")
game_is_on = True
all_states = list(data.state)
guessed_states=[]
missed_states=[]
total_guesses = 0


def analysis(guessed_states):
    missing_states = [all_states.remove(state) for state in guessed_states]
    missing_states = pandas.DataFrame(all_states)   
    missing_states.to_csv("day_25_reading_CSV_files/US_States_Quiz/states to learn")            
    print(f"You missed {all_states}")

while game_is_on:
    guess = screen.textinput(title=None,prompt="Enter a state name").title()
    for state in data['state']:
        if guess == state:
            state_row = data[data.state == guess]
            state_label = turtle.Turtle(visible=False)
            state_label.up()
            state_label.goto(state_row.x.item(),state_row.y.item())
            state_label.write(guess)
            guessed_states.append(guess)
            total_guesses+=1
        if guess == 'Exit':
            analysis(guessed_states)
            game_is_on = False
            break
        else:
            pass
        if total_guesses == 50:
            state_label.goto(0,0)
            state_label.write("YOU WIN!",font=("Arial",50,'normal'))
            game_is_on = False
            break
    if game_is_on == False:
        break
    