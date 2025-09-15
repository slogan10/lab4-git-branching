def intro():
    print("You wake up in a dark forest. You can go left,right, or center.")
    choice = input("Which direction do you choose? (left/right/center): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    elif choice == "center":
        center_path()
    else:
        print("You stand still, unsure what to do. The forest swallows you.")

def left_path():
    print("You walk left and find a mysterious glowing sword stuck in a stone.")

def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")
    print("You accept and handily defeat him, putting him in a firm headlock, then you interrogate him for the location of his acorn stash.")
    print("After he tells you the location of his stash, you bind him to a tree branch, and leave him.")
    print("You then find the hidden stash, and eat all of the acorns for yourself, leaving him and his squirrel family with nothing for the winter.")

def center_path():
    print("You walk the center path and find nothing, great job.")

if __name__ == "__main__":
    intro()
