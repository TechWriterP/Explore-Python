# Treasure Island Game - Day 3 Project

print("Welcome to Treasure Island 🏝️")
print("Your mission is to find the treasure. 💎")

# First choice
choice1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right': ").lower()

if choice1 == "left":
    # Second choice
    choice2 = input("You've come to a lake. Type 'wait' to wait for a boat. Type 'swim' to swim across: ").lower()
    
    if choice2 == "wait":
        # Third choice
        choice3 = input("You arrive at the island unharmed. "
                        "There is a house with 3 doors: red, yellow, and blue. "
                        "Which color do you choose? ").lower()
        
        if choice3 == "yellow":
            print("🎉 You found the treasure! You win! 🏆")
        elif choice3 == "red":
            print("🔥 It's a room full of fire. Game Over.")
        elif choice3 == "blue":
            print("🐉 You enter a room of beasts. Game Over.")
        else:
            print("🚪 You chose a door that doesn't exist. Game Over.")
    else:
        print("🦈 You got attacked by an angry trout. Game Over.")
else:
    print("😵 You fell into a hole. Game Over.")
