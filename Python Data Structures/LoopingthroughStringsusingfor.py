#Looping through Strings using 'for'
fruit = input('Enter a fruit:')
index = 0
for letter in fruit :
    print(index, letter)
    index = index + 1
x = len(fruit)
print('The lenghth of fruit is',x)