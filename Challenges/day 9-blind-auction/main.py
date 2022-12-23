from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
import random
print(logo)
print("Welcome to the secret auction program.") 
keep = True
audict={} 
names=[]
bids=[]
while keep:
  
  key = input("What is your name?:")
  value = int(input("What's your bid?: $"))
  i =0
  names.append(key)
  bids.append(value)
  for name in names:
    audict[name] = bids[i]
    i+=1
  clearing = input("Are there any other bidders? Type 'yes' or   'no'.").lower()
  
  if clearing == "yes":
    keep = True
    clear()
  elif clearing == "no":
    keep = False
    
    win_list=[]
    for bid in audict:
      amount = audict[bid]
      
      if max(bids)==amount:
        win_list += {bid}
        biggest = amount
if len(win_list) ==1:
    print(f"The winner is {bid} with a bid of {biggest}")
else:  
    winner = win_list[random.randint(0,len(win_list)-1)]
    print(f"Auction draw, the winner was drawn. The winner is {winner} with a bid of {biggest}.")       
      

