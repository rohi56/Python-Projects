#Strippning Whitespace
opt = 'yes'
while opt == 'yes' :
    word = input('Enter a string with spaces to play with stripping whitespaces: ')
    choice = input('Select where you want to strip(left/right/centre): ')
    if choice == 'left' :
        print('left stripping :',word.lstrip())
    
    elif choice == 'right' :
        print('right stripping :',word.rstrip())

    elif choice == 'centre' :
        print('centre stripping :',word.strip())

    else :
        print('You have enter wrong input')
        opt = input('Do you want to try again (yes/no): ')

print('Exiting the program. Thank You')

