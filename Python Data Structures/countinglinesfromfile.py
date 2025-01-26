#program for counting lines from file
fhandle = open ('C:\python\mbox.txt')
count = 0
for line in fhandle :
    count = count + 1
print('Line Count is :', count)