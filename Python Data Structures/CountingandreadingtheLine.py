# Counting and Reading the Lines in a File

# Open the file in read mode
fhandle = open('C:\\python\\mbox-short.txt', 'r')  
count = 0

# Count the number of lines in the file
for line in fhandle:
    count = count + 1
print('Line Count is:', count)

# Reset the file pointer to the beginning of the file
fhandle.seek(0)

# Read the entire content of the file
imp = fhandle.read()

# Print the length of the file content
print('Total Characters:', len(imp))

# Print the first 20 characters of the file content
print('First 20 Characters:', imp[:20])

# Close the file
fhandle.close()
