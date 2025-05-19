# Get user financial details
monthly_income = int(input('Enter your monthly income:'))
monthly_expenses = int(input('Enter your total monthly expenses:'))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings
annual_interest = 0.05
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest)

# Print results
print(f'Your monthly savings are ${monthly_savings}.')
print(f'Projected savings after one year, with interest, is: ${round(projected_savings)}.')