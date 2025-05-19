# Get user financial details
getIncome = int(input('Enter your monthly income:'))
getTotalExpenses = int(input('Enter your total monthly expenses:'))

# Calculate monthly savings
monthlySavings = getIncome - getTotalExpenses

# Project annual savings
annualInterest = 0.05
projectedSavings = monthlySavings * 12 + (monthlySavings * 12 * annualInterest)

# Print results
print(f'Your monthly savings are ${monthlySavings}.')
print(f'Projected savings after one year, with interest, is: ${projectedSavings}.')