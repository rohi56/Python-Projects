# Looping and counting occurrences of a letter in a string
fruit = input('Enter a fruit: ')
letter_to_count = input('Enter the letter you want to count: ')

# Initialize the count variable
count = 0

# Loop through each character in the fruit string
for char in fruit:
    if char == letter_to_count:  # Check if the current character matches the input letter
        count = count + 1

# Display the result
if count > 0:
    print(f'The count of "{letter_to_count}" in "{fruit}" is: {count}')
else:
    print(f'The letter "{letter_to_count}" is not present in "{fruit}".')
