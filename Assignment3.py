#Task 1: Calculate Factorial Using a Function 

'''
Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
n = int(input("Enter a number to find the factorial: "))
print("The factorial of",n, "is", factorial(n))



#Task 2: Using the Math Module for Calculations
'''
Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
   - Square root of the number
   - Natural logarithm (log base e) of the number
   - Sine of the number (in radians)
3.   Displays the calculated results.

'''
import math
num = int(input("Enter a number for task 2: "))
sqrt_num = math.sqrt(num)
print("Square root: ", sqrt_num)

log_num = math.log(num)
print("Natural logarithm: ", log_num)

# Convert the number to radians and calculate the sine
sin_num = math.sin(math.radians(num))
print("Sine (in radians): ", sin_num)