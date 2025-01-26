#Parsing and Extracting
word = input('Enter the string or sentence :')
start = input('Enter the first character you have to find : ')
atpos = word.find(start)
sppos = word.find(' ',atpos)
host = word[atpos:sppos]
print(host)