#Skipping with continue example
fhandle = open('C:\\python\\mbox-short.txt', 'r')  
for line in fhandle :
    line=line.rstrip()
    if not '@uct.ac.za' in line :
        continue
    print(line)
    