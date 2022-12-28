from art import logo,vs
from game_data import data
from replit import clear
import random
print(logo)

def comparation():
  loop = True
  score = 0
  A = random.choice(data)
  while loop:
    
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
    print(vs)  
    B = random.choice(data)
    if B == A:
      B = random.choice(data)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")
    follower_guess = input("Who has more followers? Type 'A' or 'B':").upper()
    if follower_guess == "A" and A['follower_count'] > B['follower_count']:
      score += 1
      clear()
      print(logo)
      print(f"You're right! Current score: {score}")
      A = B
      B = random.choice(data)
      loop = True
    
    elif follower_guess == "A" and A['follower_count'] < B['follower_count']:
      print(f"Sorry, that's wrong. Final score: {score}")
      loop = False
    elif follower_guess == "B" and A['follower_count'] < B['follower_count']:
      score += 1
      clear()
      print(logo)
      print(f"You're right! Current score: {score}")
      loop = True
      A = B
      B = random.choice(data)
      
    elif follower_guess == "B" and A['follower_count'] > B['follower_count']:
      print(f"Sorry, that's wrong. Final score: {score}")
      loop = False
    
 
comparation()
  
