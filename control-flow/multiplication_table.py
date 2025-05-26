# Get user input
number = int(input('Enter a number to see its multiplication table: '))

# Loop through the numbers
for i in range(1, 11):
  for j in range(1, 11):
    product = number * i
  print(f'{number} * {i} = {product}')