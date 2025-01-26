# 7.2 Write a program to compute the average of X-DSPAM-Confidence values.

# Prompt the user to enter the file name
fname = input("Enter file name: ")

try:
    # Open the file
    fh = open(fname)  ,
except FileNotFoundError:
    print("File not found:", fname)
    quit()

count = 0  # To count the number of lines with the required pattern
total = 0.0  # To accumulate the floating-point values

# Read through the file line by line
for line in fh:
    # Look for lines that start with "X-DSPAM-Confidence:"
    if line.startswith("X-DSPAM-Confidence:"):
        # Find the position of the number and extract it
        start = line.find(":") + 1
        value = float(line[start:].strip())
        
        # Accumulate the value and increment the count
        total += value
        count += 1

# Compute the average if at least one line was found
if count > 0:
    average = total / count
    print("Average spam confidence:", average)
else:
    print("No lines found with the pattern 'X-DSPAM-Confidence:'")

# Close the file
fh.close()
