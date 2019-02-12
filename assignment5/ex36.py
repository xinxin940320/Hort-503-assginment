from sys import exit

def eat_food():
    print ("You are really starving and want to find something to eat.")
    print("There are some bread and other ingradients.")
    print("What will you eat?")

    choice = input(">> ")

    if choice == "bread":
        dead("The bread is poisoned, you die!")
    elif choice =="cook for myself":
        print("Congrats, you will survive!")
        exit(0)
    else:
        print("I got no idea what that means.")

def cabin_door():
    print("After you run to your left, you see a wired cabin log.")
    print("You are hesisited if you should enter it.")
    print("What will you do?")

    choice = input(">> ")

    if choice == "open the door":
        eat_food()
    elif choice == "ignore the cabin":
        dead("You have no other way to survive.")
    else:
        print("I have no idea what you are saying.")
def witch_choice():
    print("A witch just shows up. She gives you a bottle of liquid.")
    print("What will you do with this bottle of liquid?")

    choice = input(">> ")

    if choice == "drink it":
        dead("Opps, the liquid is poisoned, you will die!")
    elif choice == "ignore it":
        print("Congrats, you win!")
        exit(0)

def start():
    print("You are in a scary dark forest.")
    print("And a bear is chasing for you.")
    print("There two ways you can run. Left or right.")

    choice = input(">> ")

    if choice == "left":
        cabin_door()
    elif choice == "right":
        witch_choice()

start()
