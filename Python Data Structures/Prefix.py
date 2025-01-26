#Prefixes
opt = 'yes'
while opt == 'yes' :
   line = input('Enter the string or sentances: ')
   prefixes = input ('Enter the value of Prefixes to check: ')
   print('Verified prefixes:', line.startswith(prefixes))
   opt = input('Do you have to continue (yes/no) : ')
print('Thank you')
