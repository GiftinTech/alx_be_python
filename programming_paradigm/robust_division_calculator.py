def safe_divide(numerator, denominator):
  
  try:
    arg1 = float(numerator)
    arg2 = float(denominator)

    if arg1 == 0 or arg2 == 0:
      raise ZeroDivisionError('Error: Cannot divide by zero.')
    else:
      result = arg1 / arg2
      return f"The result of the division is {result}"

  except ValueError:
    print('Error: Please enter numeric values only.')