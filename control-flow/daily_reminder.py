# Get user input
task = input('Enter your task: ')
priority = input('Priority (high/medium/low): ').lower()
time_bound = input('Is it time-bound? (yes/no):').lower()

reminder = ''

# Process the Task Based on Priority and Time Sensitivity:
match priority:
  case 'high':
    reminder = f'Reminder: {task} is a {priority} task'
  case 'medium':
    reminder = f'Reminder: {task} is a {priority} task'
  case 'low':
    reminder = f'Reminder: {task} is a {priority} task'

if time_bound == 'yes':
  print(f'{reminder} that requires immediate attention today!')
else:
  print(f'{reminder}. Consider completing it when you have free time.')