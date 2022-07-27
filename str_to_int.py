# This is a function to demonstrate changing data type witout using the int function

num = "12345"

def int_conversion(num):
    # variable to hold the final output
    total = 0

    # incrementer for the power variable
    i = 1
    
    # The power by which to multiply each number
    power = 10 ** (len(num) - i)

    for item in num:
        # Find the integer representation of each number in the string using the ascii value, then multiply by its respective power
        x = (ord(item) - 48) * power
        total += x
        i += 1
        power = 10 ** (len(num) - i)
    return total

print(int_conversion(num))
