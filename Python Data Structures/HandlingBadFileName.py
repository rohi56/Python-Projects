#Handling Bad File Name
fname = input('Enter the file name :')
try:
    fhandle = open(fname)
except:
    print('File cannnot be opened:',fname)
    quit()
count = 0
for line in fhandle :
    if line.startswith ('Subject') :
        count = count + 1
print('The are', count, 'subject line in',fname)