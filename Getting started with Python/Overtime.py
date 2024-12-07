# Prompt the user to input the number of hours worked
hrs = input("Enter Hours:")

# Prompt the user to input the rate per hour
rate = input("Enter Rate:")

# Convert the hours input from string to integer for calculations
hrs = int(hrs)

# Convert the rate input from string to float for calculations
rate = float(rate)

# Check if hours worked exceed 40 to calculate overtime
if hrs > 40:
    # Calculate the number of overtime hours worked
    Overtime = hrs - 40
    
    # Calculate the pay for overtime hours at 1.5 times the regular rate
    Overtimepay = Overtime * (1.5 * rate)
    
    # Calculate the total pay including regular and overtime pay
    Pay = (40 * rate) + Overtimepay
else:
    # If no overtime, calculate pay at the regular rate
    Pay = hrs * rate

# Display the calculated total pay
print(Pay)
