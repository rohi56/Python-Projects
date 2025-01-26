#Slicing Strings
a = input("Do you want to slice a string (Yes/No): ")
if a == 'Yes' :
       word = input("Enter the word you want to slice: ")
       i = input ('Enter the beginning range: ')
       i = int(i)
       j = input ('Enter the ending range: ')
       j = int(j)
       print('Here is the range you have selected :',word[i:j])
elif a == 'No' :
       print('Thanks exiting the program')

else :
       print('Enter a valid input')
     