alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
print(logo)

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def caesar(plain_text,shift_amount):
      
    text_list=[]
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    for a in range(len(text)):
      text_list.append(text[a])
      if text_list[a] in alphabet:
        ind = alphabet.index(text_list[a])
        if direction == "encode":
          if shift + ind <26:
            text_list[a] = alphabet[(shift + ind)]
          else:
            while shift + ind > 26: 
              ind = ind - 26 
            text_list[a] = alphabet[(shift + ind)]
        elif direction == "decode":
          ind = alphabet.index(text_list[a])
          text_list[a] = alphabet[(ind - shift)]
      else:
        text_list[a] = text[a]
        
    print( ''.join(text_list)) 

repeat = "yes"    
while repeat == "yes":

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text, shift)
  repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

print("Program ended")