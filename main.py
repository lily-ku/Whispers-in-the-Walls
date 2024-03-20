import os, sys, time

# Colours
cyan = "\u001b[36m"
normal = "\u001b[0m"
green = "\u001b[32m"
red = "\u001b[31m"
reverse = "\u001b[7m"

INVENTORY = []

# Functions
def death():
    clear()
    print(f"{red}D E A T H{normal}")
    print(f"{cyan}You've offered all you could.")
    p()
    print(f"{cyan}For that, at least, you are thanked.{normal}")
    p()
    exit()

def choose(*choices):
    ind()
    for c in choices:
        print(c)
    ind()

def invalid():
    print(f"{red}That is not a choice. The game will now exit.{normal}")
    time.sleep(2)
    exit()

def p():
    time.sleep(3)

def pd(seconds):
    time.sleep(seconds)

def s():
    time.sleep(1)

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def ind():
    print("\n")

def tab():
    print(f"{reverse} Inventory: {', '.join(INVENTORY)} {normal}\n\n")

def start():
    clear()
    tab()
    print("You walk into a room, no voice greets you.")
    p()
    print("You don't remember why you're here, do you?")
    p()
    print("There's a door to your right, maybe you should check that out first.")
    p()

    choose (
        f"Check the {cyan}door {normal}to your right",
        f"Check the {cyan}art {normal}on the walls"
    )

    choice = input("Choice: ")

    if choice == "door":
        right_door()
    elif choice == "art":
        wall_art()
    else:
        invalid()

def wall_art():
    clear()
    tab()
    print("You spot drawings on the wall in the corner of your eye.")
    p()
    print("You walk to them for a closer look.")
    p()
    print("There are people drawn, seemingly in pen. It doesn't seem like it's too important.")
    p()
    print("You find a pen by your feet.")
    print(f"{green}You now have a pen.{normal}")
    INVENTORY.append("Pen")

    choose (
        f"Check the {cyan}door {normal}to your right"
    )

    choice = input("Choice: ")
    if choice == "door":
        right_door()
    else:
        invalid()

def right_door():
    clear()
    tab()
    print("You walk into a room, no voice greets you.")
    p()
    print("You don't remember why you're here, do you?")
    p()
    print("...Wait this seems oddly familiar. You were just here, weren't you?")
    p()
    print("Well, anyway, there's a door to your right, maybe you should check that out first.")
    p()

    choose (
        f"Check the {cyan}door {normal}to your right",
        f"Check the {cyan}art {normal}on the walls"
    )

    choice = input("Choice: ")
    if choice == "door":
        right_door_2()
    elif choice == "art":
        wall_art_2()
    else:
        invalid()

def wall_art_2():
    clear()
    tab()
    print("You spot drawings on the wall in the corner of your eye.")
    p()
    print("You walk to them for a closer look.")
    p()
    print("There are letters drawn, but you stare at them blankly.")
    p()
    print("You... can't read it?")
    p()
    print("Ah, well I'm sure she had a reason for that.")

    choose (
        f"Check the {cyan}door {normal}to your right"
    )

    choice = input("Choice: ")

    if choice == "door":
        right_door_2()
    else:
        invalid()

def right_door_2():
    clear()
    tab()
    print("You step into a room with an immediate change in air quality.")
    p()
    print("You can't stop coughing.")
    p()
    print("Upon trying to catch your breath, you inhale an object.")
    p()
    print(f"{red}You're choking.")
    s()
    print(f"{red}This wasn't supposed to happen, why did you have to cough so damn much!?")
    s()
    print(f"{red}Now she has to find another guy to do all this. Your weakness is shameful.{normal}")
    p()

    if "Pen" in INVENTORY:
        choose (
            f"Use the {cyan}pen{normal}",
            f"{red}Die.{normal}"
        )
    else:
        choose (
            f"{red}Die.{normal}"
        )

    choice = input("Choice: ")
    if choice == "pen":
        if "Pen" in INVENTORY:
            INVENTORY.remove("Pen")
            pen_rescue()
        else:
            invalid()
    elif choice == "die":
        death()

def pen_rescue():
    clear()
    tab()
    print("You can breathe now.")
    p()
    print("Go ahead, take a sigh of relief.")
    p()
    print("You should probably save your breath, actually.")
    p()
    print("And tend to the hole in your throat that you decided to puncture.")
    p()
    print("You enter a room with two doors, one on your left and one on your right, both with passcodes.")
    p()
    print("You must figure out each passcode.")
    p()
    print("Maybe you already know them. They're surprisingly insecure...")
    p()

    choose (
        f"Go to the {cyan}left {normal}door",
        f"Go to the {cyan}right {normal}door"
    )

    choice = input("Choice: ")

    if choice == "left":
        left_door_pass()
    elif choice == "right":
        right_door_pass()
    else:
        invalid()

def left_door_pass():
    clear()
    tab()
    print("You approach the door on your left.")
    p()
    print("What do you think the passcode is?")
    p()
    print(f"Guess very carefully. It's only 3 digits. {red}Don't mess it up.{normal}")
    p()
    print("")

    code = input("Code: ")

    if code == "123":
        left_passcode_correct()
    else:
        death()

def left_passcode_correct():
    clear()
    tab()
    print(f"You enter the passcode, it's conveniently {cyan}123{normal}...")
    p()
    print("But, that seems a bit too easy, doesn't it?")
    p()
    print("Too good to be true?")
    p()

    choose (
        f"Enter the {red}door{normal}"
    )

    choice = input("Choice: ")

    if choice == "door":
        death()
    else:
        death()

def right_door_pass():
    clear()
    print("Incomplete")
    exit()

if __name__ == "__main__":
    start()
