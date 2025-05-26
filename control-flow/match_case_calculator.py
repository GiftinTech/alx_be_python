# Get user input
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
operation_type = (input('Choose the operation (+, -, *, /): '))

result = 0

# Perform calculation
match operation_type:
  case '+':
   result = num1 + num2
  case '-':
   result = num1 - num2
  case '*': 
   result = num1 * num2
  case '/':
    if num1 and num2 != 0:
     result = num1 / num2
    else:
     result = 'Cannot divide by zero'
  case _:
    result = 'Error: Invalid operation'

print(f'The result is {result}.')