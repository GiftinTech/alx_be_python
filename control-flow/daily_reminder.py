# Get user input
task = input('Enter your task: ')
priority = input('Priority (high/medium/low): ').lower()
time_bound = input('Is it time-bound? (yes/no):').lower()

# Utilities
err_message = "something went wrong!"
first_part = f"{task} is a {priority} priority task"

# Process the Task Based on Priority and Time Sensitivity:
match priority:
  case 'high':
    reminder = 'that requires immediate attention today!'
  case 'medium':
    reminder = 'Consider completing it when you have free time.'
  case 'low':
    reminder = 'Consider completing it when you have free time.'
  case _:
    message = err_message

if time_bound == 'yes':
  reminder = f'{first_part} that requires immediate attention today!'
elif time_bound == "no":
    reminder = f'{first_part} Consider completing it when you have free time.'
else:
  message = err_message

print("Reminder: ", reminder)

