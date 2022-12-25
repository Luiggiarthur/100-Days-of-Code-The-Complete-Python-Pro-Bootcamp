############### Blackjack Project #####################
from replit import clear
import random
from art import logo
#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
def draw_initcards():  
  draw = []
  pcdraw = []
  i = 0
  while i <2:
    draw.append(cards[random.choice(cards)])
    pcdraw.append(cards[random.choice(cards)])
    i += 1
  return draw,pcdraw

def sum_cards(draw_list):
  soma = 0
  for card in draw_list:      
     soma = soma + card
  return soma  
  
def draw_card(player):
  player.append(cards[random.choice(cards)])

def ace(player_draw):
  player_sum=0
  for card in player_draw:
    
    if card == 11:
       #print("soma",player_sum) 
       index = player_draw.index(card)
       player_draw[index] = 1
       #player_sum =player_sum + card
       #print("soma corrigida: " ,player_sum_ace)
          
want2play = True
while want2play == True:

  want2play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
  
  
     
  if want2play == "y":
    want2play = True
    clear()
    print(logo)
    player_draw,pc_draw = draw_initcards()
    player_sum = sum_cards(player_draw)
    print(f"  Your cards: {player_draw}, current score: {player_sum}")
    print(f"  Computer's first card: {pc_draw[0]}")
       
    
    get_card = True
    while get_card:
      get_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
      
      if get_card == "y":
        
        draw_card(player_draw)
        player_sum = sum_cards(player_draw)
        
        if player_sum > 21:
          
          ace(player_draw)
          player_sum = sum_cards(player_draw)
          print(f"  Your cards: {player_draw}, current score: {player_sum}")
          if player_sum > 21:
            print("You went over 21. You lose")
            get_card = False
        elif player_sum < 21:
  
          player_sum = sum_cards(player_draw)
          print(f"  Your cards: {player_draw}, current score:{player_sum}")
        elif player_sum ==21:
          print(f"  Your cards: {player_draw}, current score:{player_sum}")
          print("You win!!!!!!!!")
          get_card = False  
          
      elif get_card == "n":
        get_card = False
        pc_sum = sum_cards(pc_draw)
        print(f"  Computer's score: {pc_sum}")
                
        if pc_sum < player_sum:
          while pc_sum < player_sum:
         
            draw_card(pc_draw)
            pc_sum = sum_cards(pc_draw)
          if pc_sum > 21:
              ace(pc_draw)
              pc_sum = sum_cards(pc_draw)
              if pc_sum > 21:
                print(f"  Computer's final hand: {pc_draw}, final score: {pc_sum}")
                print("Pc went over 21. You win!!!")
          elif pc_sum < 21 and pc_sum != player_sum:
              print(f"  Your final hand: {player_draw}, final score: {player_sum}")
              print(f"  Computer's final hand: {pc_draw}, final score: {pc_sum}")
              print("You lose.")
          else: 
             print(f"  Computer's final hand: {pc_draw}, final score: {pc_sum}")
             print("Game draw")
        elif pc_sum > player_sum:
          print(f"  Your final hand: {player_draw}, final score: {player_sum}")
          print(f"  Computer's final hand: {pc_draw}, final score: {pc_sum}")
          print("You lose.")    
        elif pc_sum ==player_sum:
          print(f"  Computer's final hand: {pc_draw}, final score: {pc_sum}")
          print("Game draw")
          
  elif want2play == "n":
    print("Game closed.")
    want2play = False    
  




##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

