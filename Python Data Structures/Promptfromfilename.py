#Prompt from file name
fname = input('Enter the file name :')
fhandle = open(fname)
count = 0
for line in fhandle :
    if line.startswith ('Subject') :
        count = count + 1
print('The are', count, 'subject line in',fname)
