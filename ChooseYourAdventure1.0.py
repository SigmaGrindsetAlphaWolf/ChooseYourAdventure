# Programmer: John Burke
# Date: 3.15.24
# Program: Choose Your Adventure

def start_story():
    print("Welcome to the Adventure Game!")
    print("You find yourself standing at a crossroads.")
    print("You can go left, right, or straight ahead.")

    choice = input("What do you choose? (left/right/straight): ").lower()

    if choice == "left":
        go_left()
    elif choice == "right":
        go_right()
    elif choice == "straight":
        go_straight()
    else:
        print("Invalid choice. Please try again.")
        start_story()

def go_left():
    print("You chose to go left.")
    print("You encounter a dark forest.")
    print("Do you want to enter the forest or turn back?")

    choice = input("What do you choose? (enter/turn back): ").lower()

    if choice == "enter":
        print("You venture into the forest and find a hidden treasure!")
    elif choice == "turn back":
        print("You decide to turn back and return to the crossroads.")
        start_story()
    else:
        print("Invalid choice. Please try again.")
        go_left()

def go_right():
    print("You chose to go right.")
    print("You stumble upon a cave.")
    print("Do you want to enter the cave or continue on?")

    choice = input("What do you choose? (enter/continue): ").lower()

    if choice == "enter":
        print("You enter the cave and discover a dragon!")
        print("Unfortunately, you are eaten by the dragon. Game over!")
    elif choice == "continue":
        print("You decide to continue on your journey.")
        print("You reach a beautiful meadow and enjoy the scenery.")
    else:
        print("Invalid choice. Please try again.")
        go_right()

def go_straight():
    print("You chose to go straight ahead.")
    print("You walk for a while and reach a river.")
    print("Do you want to swim across the river or look for a bridge?")

    choice = input("What do you choose? (swim/look for bridge): ").lower()

    if choice == "swim":
        print("You bravely swim across the river and reach the other side safely.")
        print("Congratulations! You've completed your adventure!")
    elif choice == "look for bridge":
        print("You search for a bridge but find none.")
        print("You decide to swim across the river.")
        print("Unfortunately, you are swept away by the current. Game over!")
    else:
        print("Invalid choice. Please try again.")
        go_straight()

# Start the story
start_story()