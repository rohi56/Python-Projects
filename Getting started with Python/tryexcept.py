# Prompt the user to enter any random number or input
temp = input("Enter any random number:")

# Try to convert the entered value to an integer
try:
    ival = int(temp)
except:
    # If an error occurs (e.g., input is not a number), set ival to -1
    ival = -1

# Check if the value of ival is greater than 0 (meaning the input is numeric)
if ival > 0:
    print("Given number is Numeric")  # Output if the input is a valid positive number
else:
    # If the value of ival is -1 or 0 (i.e., not a valid number), print that the input is a character
    print("Given input is character")
