# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Conversion functions
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User interaction
temperature = input("Enter the temperature to convert: ")
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

# Validate input
try:
    temperature = float(temperature)
except ValueError:
    raise ValueError("Invalid temperature. Please enter a numeric value.")

# Perform conversion
if unit == 'F':
    result = convert_to_celsius(temperature)
    print(f"{temperature}°F is {result}°C")
elif unit == 'C':
    result = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {result}°F")
else:
    print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")


"""
Temperature Conversion Tool

Objective: Illustrate the concept of variable scope by creating a script that converts temperatures between Celsius and Fahrenheit, using global variables to store conversion factors.

Task Description:
Create a Python script named temp_conversion_tool.py. This script will define functions to convert temperatures between Celsius and Fahrenheit, demonstrating the use of global variables to store conversion factors that are accessible within functions.

Requirements:
Define Global Conversion Factors:

- At the top of your script, define two global variables FAHRENHEIT_TO_CELSIUS_FACTOR and CELSIUS_TO_FAHRENHEIT_FACTOR to store the conversion factors (e.g., (5/9) for F to C and (9/5) for C to F, respectively).

Implement Conversion Functions:

- Write a function convert_to_celsius(fahrenheit) that takes a temperature in Fahrenheit and returns the temperature converted to Celsius.
- Write a function convert_to_fahrenheit(celsius) that takes a temperature in Celsius and returns the temperature converted to Fahrenheit.
- Inside each function, use the respective global conversion factor to perform the conversion.

User Interaction:

- Prompt the user to enter a temperature and specify whether it’s in Celsius or Fahrenheit.
- Based on the user’s input, call the appropriate conversion function and display the converted temperature.
- If the user entered a wrong input,raise an error “Invalid temperature. Please enter a numeric value.”

Guidance:
- Remember to access global variables using the global keyword if you need to modify them inside functions. However, for this task, you’ll only be reading their values.
- Use input validation to ensure that the user enters a valid temperature and unit.

Example Output (Hypothetical):
Enter the temperature to convert: 100
Is this temperature in Celsius or Fahrenheit? (C/F): F
100.0°F is 37.77777777777778°C
Or:

Enter the temperature to convert: 0
Is this temperature in Celsius or Fahrenheit? (C/F): C
0.0°C is 32.0°F
"""