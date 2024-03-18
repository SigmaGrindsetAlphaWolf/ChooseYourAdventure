# Programmer: John Burke
# Date: 3.15.24
# Program: Choose Your Adventure

from time import sleep

def start_story():
    print("You are an allied captain commanding a company of soldiers shortly after the landing of Normandy")
    sleep(0.4)
    print("Its your job to lead the company of 68 people to the Rhine through France.")
    sleep(0.5)
    print("You come to a crossroad, one way points to a village, the other to an open field")

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
    print("You hear an incoming tank battalion.")
    print("Do you want to set up an ambush or face head on?")

    choice = input("What do you choose? (ambush/head on): ").lower()

    if choice == "ambush":
        print("The Tanks roll by... you yell the order and mortar shells pierce the side of the 3 panthers, one is completely destroyed and the other 2 are incapable of fighting.")
        print("The German soldiers following the tanks open fire, 12 of your men die in the fight. You have 56 men left.")
        continue_journey_village()
    elif choice == "head on":
        print("You don't survive the incoming attack, everyone dies :(")
        end_story()
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
        continue_journey_open_field()
    elif choice == "march on":
        print("The enemy planes open fire on your exposed troops. Many are killed in the attack. You lose 20 men.")
        print("You retreat to the village for safety.")
        go_left()  # Redirect to village as a safe option
    else:
        print("Invalid choice. Please try again.")
        go_right()

def continue_journey_village():
    print("You continue your journey towards the Rhine through the village.")
    print("As you pass through the village, you encounter local resistance fighters.")
    print("They offer to join forces with you in exchange for your support in their fight against the German occupation.")
    print("Do you accept their offer or continue on your own?")

    choice = input("What do you choose? (accept/continue): ").lower()

    if choice == "accept":
        print("You agree to join forces with the resistance fighters.")
        print("Together, you coordinate ambushes and sabotage missions, significantly disrupting German operations in the region.")
        print("Your combined efforts lead to the liberation of the village and surrounding areas.")
        victory()
    elif choice == "continue":
        print("You decide to continue on your own, wary of the risks of working with local resistance.")
        print("You press onwards towards the Rhine, facing numerous challenges along the way.")
        continue_journey_village_further()
    else:
        print("Invalid choice. Please try again.")
        continue_journey_village()

def continue_journey_village_further():
    print("Your journey through the village is uneventful for a while, but you soon encounter a German patrol.")
    print("You engage in a fierce firefight, but the Germans outnumber you.")
    print("Your company suffers heavy casualties, and you are forced to retreat.")
    print("You regroup outside the village, reevaluating your strategy.")
    continue_journey()

def continue_journey_open_field():
    print("You continue your journey through the open field.")
    print("You come across a destroyed supply convoy.")
    print("Do you scavenge the supplies or avoid the area?")

    choice = input("What do you choose? (scavenge/avoid): ").lower()

    if choice == "scavenge":
        print("You scavenge the supplies from the destroyed convoy, finding ammunition, medical supplies, and rations.")
        print("Your men are grateful for the additional resources.")
        print("You continue towards the Rhine, feeling better equipped to face the challenges ahead.")
        victory()
    elif choice == "avoid":
        print("You decide to avoid the area, fearing it may be booby-trapped or guarded by enemy forces.")
        print("As you bypass the convoy, you engage with German soldiers.")
        print("Several of your men are killed or injured by the explosions.")
        print("You are forced to backtrack and find an alternate route, delaying your progress.")
        continue_journey()
    else:
        print("Invalid choice. Please try again.")
        continue_journey_open_field()

def victory():
    print("Congratulations! You successfully lead your company to the Rhine


