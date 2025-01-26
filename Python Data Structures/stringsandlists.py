#strings and lists
words = 'Lets learn python today'
listwords = words.split()
print(listwords)
print(listwords[3])
#Lets use for loop
for w in listwords :
    print(w)


line = 'first;second;third'
val = line.split()
print(val)
print(len(val))

#using delimiter to split
de = line.split(';')
print(de)
print(len(de))