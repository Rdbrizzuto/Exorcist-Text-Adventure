import random 

def main():
    welcome()
    print("HOUSE LAYOUT (as drawing??)\nYou are currently in the living room\n")

    class Ghost:
        def __init__(self, EMF, UVlight, temp, pic, name):
            self.EMF = EMF
            self.UVlight = UVlight
            self.temp = temp
            self.pic = pic
            self.name = name

# defines all the types of ghosts that can haunt the house, and randomly selects one for the game
    wraith = Ghost(True, False, True, False, "wraith")
    vengeful_spirit = Ghost(True, True, False, False, "vengeful spirit")
    demon = Ghost(True, False, False, True, "demon")
    shade = Ghost(False, True, True, False, "shade")
    specter = Ghost(False, False, True, True, "specter")
    poltergeist = Ghost(False, True, False, True, "poltergeist")

    ghost_types = [wraith, vengeful_spirit, demon, shade, specter, poltergeist]

# selects the ghost and haunted room for the game, then starts the actual game
    current_ghost = random.choice(ghost_types)
    haunted_room = pick_room()
    playing(current_ghost, haunted_room)

# this is where you guess what the type of ghost is, and find out if you are wrong or right

    input_guess = input("What type of ghost is haunting this house?\n1. Wraith\n2. Vengeful spirit\n3. Demon\n4. Shade\n5. Specter\n6. Poltergeist\n\n")

    while True:
        if input_guess == "1":
            actual_guess = "wraith"
            break
        
        elif input_guess == "2":
            actual_guess = "vengeful spirit"
            break

        elif input_guess == "3":
            actual_guess = "demon"
            break

        elif input_guess == "4":
            actual_guess = "shade"
            break

        elif input_guess == "5":
            actual_guess = "specter"
            break

        elif input_guess == "6":
            actual_guess = "poltergeist"
            break

        else:
            ("Please enter a valid response")

    if actual_guess == current_ghost.name:
        print("Correct! Your boss is going to be so proud")

    else:
        print(f"Wrong! It was a {current_ghost.name}. Better start looking for a new job...")




# Welcomes you to the game. Here you can either ask for a game explanation or start a game
def welcome():
    while True:
        print('Welcome to "Assistant to the Regional Exorcist"')
        mainMenuChoice = input("1. Start game\n2. Game Explanation\n\n")

        if mainMenuChoice == "1":
            break 

        elif mainMenuChoice == "2":
            explain_game()
        
        else:
            print('Invalid input, please type "1" or "2"\n')

# explains the rules of the game and how it is played
def explain_game():
    print("EXPLANATION\n")
    input('Press "Enter" to continue\n')


# randomly picks which room the ghost will haunt
def pick_room():
    all_rooms = ["living room", "dining room", "kitchen", "bedroom", "bathroom", "garage"]
    haunted_room = random.choice (all_rooms)

    return haunted_room

# which rooms can you move into from the room you are in
def change_rooms(current_room):
    if current_room == "living room":
        choice = input("Which room would you like to move into?\n1. Bedroom\n2. Dining room\n3. Garage\n\n")
        while True:
            if choice == "1":
                current_room = "bedroom"
                break

            elif choice == "2":
                current_room = "dining Room"
                break
            
            elif choice == "3":
                current_room = "garage"
                break

            else:
                ("Please enter a valid response")

    elif current_room == "bedroom":
         choice = input("Which room would you like to move into?\n1. Bathroom\n2. Living room\n\n")
         while True:
            if choice == "1":
                current_room = "bathroom"
                break

            elif choice == "2":
                current_room = "living Room"
                break

            else:
                ("Please enter a valid response")

    elif current_room == "bathroom":
         choice = input("Which room would you like to move into?\n1. Bedroom\n\n")
         while True:
            if choice == "1":
                current_room = "bedroom"
                break

            else:
                ("Please enter a valid response")


    elif current_room == "dining room":
        choice = input("Which room would you like to move into?\n1. Kitchen\n2. Garage\n3. Living room\n\n")
        while True:
            if choice == "1":
                current_room = "kitchen"
                break

            elif choice == "2":
                current_room = "garage"
                break
            
            elif choice == "3":
                current_room = "living room"
                break

            else:
                ("Please enter a valid response") 

    elif current_room == "kitchen":
        choice = input("Which room would you like to move into?\n1. Dining room\n\n")
        while True:
            if choice == "1":
                current_room = "dining room"
                break

            else:
                ("Please enter a valid response") 

    elif current_room == "garage":
        choice = input("Which room would you like to move into?\n1. Living room\n2. Dining room\n\n")
        while True:
            if choice == "1":
                current_room = "living room"
                break

            elif choice == "2":
                current_room = "dining Room"
                break

            else:
                ("Please enter a valid response") 


    return current_room


# the choices you can make playing (Move, Ghost type checks, Consult diary, Guess)
def playing(current_ghost, haunted_room):
    time_left = 150
    current_room = "living room"

    while time_left > 0:
        choice = input("What do you want to do?\n1. Move to a different room\n2. Check room's EMF\n3. Shine UV light around room\n4. Check room's temperature\n5. Take a photo of the room\n6. Consult Paranormal Encyclopedia\n7. Guess ghost\n\n")

        # moving to a different location
        if choice == "1":
            current_room = change_rooms(current_room)
            print(f"You have entered the {current_room}\n")
        
        # check EMF
        elif choice == "2":
            if (current_room == haunted_room) and (current_ghost.EMF == True):
                print("The EMF reader is going crazy!\n")
            else:
                print("Barely even a beep from your EMF reader...\n")
            time_left = time_left - 10

        # check for fingerprints with UV
        elif choice == "3":
            if (current_room == haunted_room) and (current_ghost.UVlight == True):
                print("As you shine your UV light on the wall next to you, you see the outline of a hand\n")
            else:
                print("You shine the light all over, but don't see anything out of place\n")
            time_left = time_left - 10

        # check temperature of room
        elif choice == "4":
            if (current_room == haunted_room) and (current_ghost.temp == True):
                print("Your thermometer reads zero degrees...\n")
            else:
                print("Its a normal room temp in here\n")
            time_left = time_left - 10
        
        # take photo of the room
        elif choice == "5":
            if (current_room == haunted_room) and (current_ghost.pic == True):
                print("As you look at the photo that you just took, you notice a silhouette crouching in the corner!\n")
            else:
                print("You can't find anything out of place in the photo you took\n")
            time_left = time_left - 10

        # consult encyclopedia
        elif choice == "6":
            print("ENCYCLOPEDIA")
            input('Press "Enter" to continue\n')

        # guess ghost
        elif choice == "7":
            print("Well aren't you confident...")
            break

        else:
            print("Please enter a valid choice")

main()
