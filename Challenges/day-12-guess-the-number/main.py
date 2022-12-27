#Number Guessing Game Objectives:
from art import logo
import random
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

def number():
  '''defines the correct number'''
  ans_number = random.randint(1,100)
  return ans_number

def comparsion(ans_number):
  '''compares the correct number and the guessing number'''
  global attempts

  if attempts == 0:
    return
       
  elif ans_number == guess:
    return 
      
  elif ans_number > guess:
    print("Too low.")
    print("Guess again.")
    print(f"You have {attempts} attempts remaining to guess the number.")
      
  elif ans_number < guess:
    print("Too high.")
    print("Guess again.")
    print(f"You have {attempts} attempts remaining to guess the number.")

def choose_difficulty(difficulty):
  '''selects the difficulty of the game'''
  if difficulty == "easy":
    print("You have 10 attempts remaining to guess the number.")
    attempts = 10
  elif difficulty== "hard":
    print("You have 5 attempts remaining to guess the number.")
    attempts = 5
    
  return attempts 
  
ans_number = number()
#print(f"Pssst, the correct answer is {ans_number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
attempts = choose_difficulty(difficulty)
guess =""

while attempts != 0:

  if attempts >0:
    guess = int(input("Make a guess: "))
    attempts -= 1
    comparsion(ans_number)      
             
    if attempts == 0 and ans_number != guess:  
      print("You've run out of guesses, you lose.")
    elif attempts == 0 and ans_number == guess:
      print(f"You got it! The answer was {ans_number}.")
    elif ans_number == guess:
      print(f"You got it! The answer was {ans_number}.")
    
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).