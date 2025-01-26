#Searching Through File(fixed)
# Open the file in read mode
fhandle = open('C:\\python\\mbox-short.txt', 'r')  
for line in fhandle :
    line=line.rstrip()
    if line.startswith('From') :
        print(line)
    