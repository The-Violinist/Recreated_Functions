# My first experience with creating a class and methods.

# This is a simple class with methods which perform basic mathematical operations
class my_first_class():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(num1, num2):
        return (num1 + num2)
    def subtract(num1, num2):
        return (num1 - num2)
    def multiply(num1, num2):
        return (num1 * num2)
    def divide(num1, num2):
        return (num1 / num2)

# Take user input for 2 numbers to demonstrate the 4 basic math operations
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))

# Using the my_first_class with each of the 4 methods
print(f"Adding: {my_first_class.add(num1, num2)}")
print(f"Subtracting: {my_first_class.subtract(num1, num2)}")
print(f"Multiplying: {my_first_class.multiply(num1, num2)}")
print(f"Dividing: {my_first_class.divide(num1, num2)}")
