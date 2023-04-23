
def main():
    welcome()
    start_game()
    
    # should there be a function most the game takes place in. Or should that just be main (how can a loop good in main?)
    # how do I track "time left" when using many functions ?



# Welcomes you to the game. Here you can either ask for a game explanation or start a game
def welcome():
    while True:
        print('Welcome to "Assistant to the Regional Exorcist"')
        mainMenuChoice = input("1. Start game\n2. Game Explanation")

        if mainMenuChoice == "1":
            break 

        elif mainMenuChoice == "2":
            return
        
        else:
            print('Invalid input, please type "1" or "2"')

# explains the game. Press a button to end function
def explain_game():

# explains the layout of the house. Has you enter the front door. Returns the randomly selected ghost and total time
def start_game():
    #start here

# the standard choices this game presents you (Move, Ghost type checks, Consult diary, Guess)
def action_choices():
    #start here

# ends the game early, and allows you to guess what ghost it is. If you get it right you win, if not you lose
def guess_ghost():
    #start here

# subtracts the time it takes to perform an action and returns the total time left
def time_left():
    #start here
