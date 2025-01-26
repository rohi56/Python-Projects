#Searching a String
opt = 'Yes'
while opt == 'Yes' :
    word = input ('Enter the string :')
    searchstring = input('Enter the search string you want to find :')
    result = word.find(searchstring)
    print('Your sring starts at :',result)
    opt = input ('Do you want to continue (Yes/No) :')
print('Exiting the program')
                 