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

def go_right():
    print("You chose to lead your troops to the open field.")
    print("You spot a squadron of German planes approaching.")
    print("Do you order your troops to take cover or continue marching?")

    choice = input("What do you choose? (take cover/march on): ").lower()

    if choice == "take cover":
        print("You order your troops to take cover. The enemy planes strafe the field with machine gun fire, but your men avoid casualties by hiding in nearby trenches.")
        print("Once the planes have passed, you resume marching with all your men intact.")
        continue_journey()
    elif choice == "march on":
        print("The enemy planes open fire on your exposed troops. Many are killed in the attack. You lose 20 men.")
        print("You retreat to the village for safety.")
        go_left()  # Redirect to village as a safe option
    else:
        print("Invalid choice. Please try again.")
        go_right()
def continue_journey():
    print("You continue your journey through the open field.")
    print("Suddenly, you encounter a minefield.")
    print("Do you attempt to navigate through the minefield or find an alternate route?")

    choice = input("What do you choose? (navigate/alternate route): ").lower()

    if choice == "navigate":
        print("Your company successfully navigates through the minefield with minimal casualties.")
        print("You proceed towards the Rhine.")
        victory()
    elif choice == "alternate route":
        print("You spend extra time finding an alternate route, avoiding the minefield entirely.")
        print("However, this delay allows enemy reinforcements to catch up with you.")
        print("You engage in a fierce battle but suffer heavy casualties.")
        print("Only a few of your men manage to reach the Rhine.")
        defeat()
    else:
        print("Invalid choice. Please try again.")
        continue_journey()

def victory():
    print("Congratulations! You successfully lead your company to the Rhine.")
    print("Your bravery and strategic decisions ensured the safety of your men.")
    print("You are hailed as a hero and receive commendations for your leadership.")
    end_story()

def defeat():
    print("Despite your efforts, the enemy overwhelms your company.")
    print("You fight valiantly but are ultimately forced to surrender.")
    print("Your remaining men are taken as prisoners of war.")
    end_story()

def end_story():
    print("The war may be over for now, but your actions will be remembered.")
    print("Thank you for playing!")

# Start the story
start_story()


