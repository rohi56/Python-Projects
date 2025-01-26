#lower and upper case:
word = input('Enter the string : ')
lowerupper = input ('Do you wamt the sring in lower case or upper case (lower/upper) :')
if lowerupper == 'lower' :
    print(word.lower())
elif lowerupper == 'upper' :
    print(word.upper())
else :
    print('You have not enter valid input')