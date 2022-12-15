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

#Write your code below this line 👇
import random

person = input("What do you choose? Type 0 for Rock, 1 for Paper , 2 for Scissors.\n")

computer = random.randint(0,2)

if person == "0": #rock
  print(rock)
  if computer == 0:
    print("Computer choose:\n", rock)
    print("Draw")
  elif computer == 1:
    print("Computer choose:\n",paper)
    print("You lose")
  else:
    print("Computer choose:\n",scissors)
    print("You win")

elif person == "1": #paper
  print(paper)
  if computer == 0:
    print("Computer choose:\n", rock)
    print("You win")
  elif computer == 1:
    print("Computer choose:\n",paper)
    print("Draw")
  else:
    print("Computer choose:\n",scissors)
    print("You lose")

elif person == "2": #scissors
  print(scissors)
  if computer == 0:
    print("Computer choose:\n", rock)
    print("You lose")
  elif computer == 1:
    print("Computer choose:\n",paper)
    print("You win")
  else:
    print("Computer choose:\n",scissors)
    print("Draw")
else:
  print("invalid number, choose between 0 and 2")