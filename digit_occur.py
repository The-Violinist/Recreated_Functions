arr = [25, 2, 17, 94, 38, 56, 3]

# Dictionary for the occurrences of each digit
nums_dict = {
    "0":0,
    "1":0,
    "2":0,
    "3":0,
    "4":0,
    "5":0,
    "6":0,
    "7":0,
    "8":0,
    "9":0,
}

# Populate the dictionary with the occurrences of each digit
for item in arr:
    num_str = str(item)                                                                     # Turn the list item into a string
    for character in num_str:
        nums_dict[character] = nums_dict[character] + 1                                     # Increment the dict value for the digit

max_keys = [key for key, val in nums_dict.items() if val == max(nums_dict.values())]        # Create list of the highest occurring key(s)

max_occur = []                                                                              # List for the final integers which occur the most
for num in max_keys:
    max_occur.append(int(num))                                                              # Add each integer to the final list
print(max_occur)