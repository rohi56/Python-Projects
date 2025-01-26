#Skipping with continue
fhandle = open('C:\\python\\mbox-short.txt', 'r')  
for line in fhandle :
    line=line.rstrip()
    if not line.startswith('From') :
        continue
    print(line)
    