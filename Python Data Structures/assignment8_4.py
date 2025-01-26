# Open the file romeo.txt
fname = input("Enter file name: ")
fh = open(fname)
words_list = []  # Initialize an empty list for words

    # Read the file line by line
for line in fh :
        # Split the line into words
        words = line.split()
        for word in words:
            # Add the word to the list if not already present
            if word not in words_list:
                words_list.append(word)

# Sort the resulting list in alphabetical order
words_list.sort()

# Print the sorted list of words
print(words_list)
