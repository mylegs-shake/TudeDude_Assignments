'''Task 1: Check if a Number is Even or Odd
Problem Statement:  Write a Python program that:
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.
'''
a = int(input(f"Enter an integer: "))
if a % 2 == 0:
    print(f"{a} is an even number.")
else:
    print(f"{a} is an odd number.")
    
'''    
Task 2: Sum of Integers from 1 to 50 Using a Loop
 
Problem Statement: Write a Python program that:
1.   Uses a for loop to iterate over numbers from 1 to 50.
2.   Calculates the sum of all integers in this range.
3.   Displays the final sum.
'''
sum=0
for i in range(1,51):
    sum += i
print("The sum of 1 to 51 numbers is: ",sum)