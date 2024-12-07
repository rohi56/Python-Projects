# Define the function to compute pay
def computepay(hours, rate):
    if hours > 40:
        # Calculate overtime pay
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * (1.5 * rate)
        # Calculate total pay (regular + overtime)
        total_pay = (40 * rate) + overtime_pay
    else:
        # Calculate regular pay
        total_pay = hours * rate
    return total_pay

# Prompt the user for hours and rate
hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")

# Convert input strings to float
hrs = float(hrs)
rate = float(rate)

# Call the function to compute pay and store the result
gross_pay = computepay(hrs, rate)

# Print the computed gross pay
print("Pay:", gross_pay)
