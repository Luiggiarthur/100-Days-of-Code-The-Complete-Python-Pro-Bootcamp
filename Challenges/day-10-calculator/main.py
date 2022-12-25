from art import logo

def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

def exponencial(n1,n2):
  return n1**n2
def root(n1,n2):
  return n1**(1/n2)

def percentage(n1,n2):
  return (n1/100)*n2 

operations = {
  "+":add,        
  "-":subtract,
  "*":multiply,
  "/":divide,
  "exp":exponencial,
  "root":root,
  "%":percentage,
}
def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  continuation = True
  for symbol in operations:
    print(symbol)
    
  while continuation:  
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the second number?: "))
    
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    continuation = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation. ").lower()
    if continuation == "y":
      num1 = answer  
    elif continuation == "n":
      continuation = False
      calculator()
calculator()      