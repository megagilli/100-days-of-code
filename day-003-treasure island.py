print(''' 
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
''')

print("Welcome to the Treasure Island!")
print("Your mission is to find the Treasure!")

# First choice
dir = input("You're at a crossroad. Which way do you want to go? Type 'left' or 'right': ").lower()

if dir == "left": 
    # Second choice
    action = input("You have reached a lake shore. There is an island in the middle of the lake. Do you want to swim or wait for the boat? Type 'swim' or 'wait': ").lower()
    
    if action == "wait":
        print("You made it to the island safely!")
        # Third choice
        door = input("The castle on the island has three doors. Which one do you want to enter? Type 'red', 'blue', or 'yellow': ").lower()
        
        if door == "yellow":
            print("You found the treasure! You won!!")
        elif door == "red":
            print("You entered a room full of fire. Game over!")
        elif door == "blue":
            print("You entered a room of beasts. Game over!")
        else:
            print("Such a door exists only in your imagination!")
    
    elif action == "swim":
        print("You swam without knowing the river had saltwater crocodiles!")
        print("Game over!")
    else:
        print("Invalid choice. Game over!")

else: 
    print("There was a pit on the right side, and you fell inside!")
    print("Game over!")
