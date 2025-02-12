#matching and extracting the data
x = input('Enter x string with a number: ')
y = input('Enter y string with a number: ')
import re
z1 = re.findall('[0-9]+', x)
z2 = re.findall('[0-9]+', y)
print('Output of x :', z1)
print('Output of y :', z2)

z3 = re.findall('[AEIOU]+', x)
z4 = re.findall('[AEIOU]+', y)
print('Uppercase Vowel in of x :', z3)
print('Uppercase Vowel in of y :', z4)