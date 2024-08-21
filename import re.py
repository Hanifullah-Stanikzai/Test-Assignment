import re

# Update with the correct file path
file_path = 'E:\\Pyt\\regex_sum_1980844.txt'  # Make sure to use double backslashes or a raw string

# Initialize sum
total_sum = 0

# Open and read the file
with open(file_path, 'r') as file:
    for line in file:
        # Find all numbers in the current line
        numbers = re.findall('[0-9]+', line)
        # Convert each found number to integer and add to total_sum
        total_sum += sum(int(number) for number in numbers)

print("The sum of all numbers is:", total_sum)