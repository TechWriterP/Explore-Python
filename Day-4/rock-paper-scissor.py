import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_input = int(input("What do you choose?\n Type 0 for Rock, 1 for Paper, or 2 for scissors.\n"))
if user_input == 0:
    print(rock)
elif user_input == 1:
    print(paper)
elif user_input == 2:
    print(scissors)
else:
    print("Wrong Input")

comp_input = int(random.randint(0,2))
print(f"Comp chose: {comp_input}")

if comp_input == 0:
    print(rock)
elif comp_input == 1:
    print(paper)
elif comp_input == 2:
    print(scissors)
else:
    print("Wrong Input")

if user_input == comp_input:
    print("It is a draw")
elif user_input == 0 and comp_input == 1:
    print("Comp wins")
elif user_input == 1 and comp_input == 2:
    print("Comp wins")
elif user_input == 2 and comp_input == 0:
    print("Comp wins")
elif user_input == 1 and comp_input == 0:
    print("You win")
elif user_input == 2 and comp_input == 1:
    print("You win")
elif user_input == 0 and comp_input == 2:
    print("You win")