# Prompt the user to input the number of hours worked
hrs = input("Enter Hours:")

# Prompt the user to input the rate per hour
rate = input("Enter Rate:")

# Convert the hours input from string to integer
hrs = int(hrs)

# Convert the rate input from string to float
rate = float(rate)

# Calculate the total pay by multiplying hours worked with the hourly rate
Pay = hrs * rate

# Display the calculated pay
print('Pay:', Pay)