# Get user input
size = int(input('Enter the size of the pattern: '))

# Init the pattern
pattern = 0

# Iterate through each row and print the asterics
while pattern < size:
  for i in range(size):
    print('*', end='')
  print()
  pattern += 1