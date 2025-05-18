def start_adventure():
    print("You wake up in a dark forest. You can hear the rustling of leaves and the distant hoot of an owl.")
    print("There are two paths ahead of you:")
    print("1. Take the path to the left.")
    print("2. Take the path to the right.")

    choice = input("What do you do? (Enter 1 or 2): ")

    if choice == "1":
        left_path()
    elif choice == "2":
        right_path()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        start_adventure() # Go back to the start

def left_path():
    print("\nYou walk down the left path and come to a small stream.")
    print("You can either:")
    print("1. Try to cross the stream.")
    print("2. Follow the stream bank.")

    choice = input("What do you do? (Enter 1 or 2): ")

    if choice == "1":
        print("\nYou try to cross the stream but slip and fall. You get wet and decide to turn back.")
        start_adventure()
    elif choice == "2":
        print("\nYou follow the stream bank and eventually find a bridge. You cross safely.")
        reach_clearing()
    else:
        print("Invalid choice.")
        left_path()

def right_path():
    print("\nYou take the right path and find a hidden cave entrance.")
    print("Do you:")
    print("1. Enter the cave.")
    print("2. Continue past the cave.")

    choice = input("What do you do? (Enter 1 or 2): ")

    if choice == "1":
        enter_cave()
    elif choice == "2":
        print("\nYou continue past the cave and the path eventually leads back to where you started.")
        start_adventure()
    else:
        print("Invalid choice.")
        right_path()

def reach_clearing():
    print("\nYou reach a sunny clearing. In the center, you see a mysterious chest.")
    print("Do you:")
    print("1. Open the chest.")
    print("2. Leave the chest and continue exploring.")

    choice = input("What do you do? (Enter 1 or 2): ")

    if choice == "1":
        print("\nYou open the chest and find a pile of gold! Congratulations, you found treasure!")
    elif choice == "2":
        print("\nYou decide to leave the chest and continue your adventure (which ends here for now!).")
    else:
        print("Invalid choice.")
        reach_clearing()

def enter_cave():
    print("\nYou cautiously enter the dark cave. You hear a dripping sound.")
    print("Suddenly, you encounter a friendly bat!")
    print("The bat offers to guide you out of the forest.")
    print("Do you:")
    print("1. Accept the bat's offer.")
    print("2. Politely decline and try to find your own way.")

    choice = input("What do you do? (Enter 1 or 2): ")

    if choice == "1":
        print("\nThe bat guides you out of the forest. You are safe!")
    elif choice == "2":
        print("\nYou try to find your own way but get lost. The adventure ends here.")
    else:
        print("Invalid choice.")
        enter_cave()

if __name__ == "__main__":
    start_adventure()