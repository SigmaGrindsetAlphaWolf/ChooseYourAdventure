# Programmer: John Burke
# Date: 3.15.24
# Program: Choose Your Adventure

from time import sleep

def start_story():
    print("You are an allied captain commanding a company of soldiers shortly after the landing of Normandy")
    sleep(0.4)
    print("Its your job to lead the company of 68 people to the Rhine through France.")
    sleep(0.5)
    print("You come to a crossroad, one way points to a village the other, to an open field")

    choice = input("What do you choose? (village/open field): ").lower()

    if choice == "village":
        go_left()
    elif choice == "open field":
        go_right()
    else:
        print("Invalid choice. Please try again.")
        start_story()

def go_left():
    print("You chose to lead your troops to the village.")
    print("You hear an incoming tank battalion")
    print("Do you want to set up an ambush or face head on?")

    choice = input("What do you choose? (ambush/head on): ").lower()

    if choice == "ambush":
        print("The Tanks roll by... you yell the order and mortar shells pierce the side of the 3 panthers, one is completely destroyed and the other 2 are incapable of fighting")
        print("The German soldiers following the tanks open fire, 12 of your men die in the fight. You have 56 men left")
    elif choice == "head on":
        print("You dont survive the incoming attack, everyone dies :(")
        start_story()
    else:
        print("Invalid choice. Please try again.")
        go_left()

# Start the story
start_story()
