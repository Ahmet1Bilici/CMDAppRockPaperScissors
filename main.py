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
# Start game
print("You think you can beat me!! Huh, how dare you peasant!")

# Save Rock Paper and Scissors text displays into array
moves = ["rock", "paper", "scissors"]
display_texts = [rock, paper, scissors]

# Get user input and generate pc input and print relevant move display
user_input = int(input("Play your hand! (0 for Rock, 1 for Paper, 2 for Scissors)\n"))
if user_input < 0 or user_input > 2:
    print("I said enter 0, 1 or 2!! You entered invalid number! Get Lost!")
    quit()

print("\n")

print(f"You played {moves[user_input]}\n{display_texts[user_input]}")
pc_input = random.randint(0,2)
print(f"I played {moves[pc_input]}\n{display_texts[pc_input]}")

#Rock beat scissors
#Paper beats rock
#Scissors beats paper

# Check result
if user_input == pc_input:
    print("RESULT: DRAW.\nYou are lucky that I didn't beat you today!")
elif (user_input == 0 and pc_input == 2) or (user_input == 1 and pc_input == 0) or (user_input == 2 and pc_input == 1):
    print("RESULT: YOU WON\nHOW HOW HOW!!! You are definetly using black magic!!!")
else:
    print("RESULT: YOU LOSt\nHA HA HA!!! Of course I've beaten you! Know your place!!!")

print("\n\n")

