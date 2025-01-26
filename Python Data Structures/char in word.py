#Program to check number of repeated character in word
word = input("Enter a word:")
character = input("Enter the character you want to count in word:")
count = 0
for letter in word :
    if letter == character :
        count = count + 1

print(count,'times the character is present in :', word)
        