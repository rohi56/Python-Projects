# Checking the ASCII value of characters in a string

input_string = input("Enter a string: ")

for char in input_string:
    print(f"The ASCII value of '{char}' is {ord(char)}")