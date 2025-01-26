#Sorting lists of tuples
d = {'a':10, 'c':22, 'b':1}
for k,v in d.items():
    print(k,v)
print(sorted(d.items()))

print ('Sorting by keys :')
for k,v in sorted(d.items()):
    print(k,v)
tmp = list()
for k,v in sorted(d.items()):
    tmp.append((v,k))

print(sorted(tmp))
print("sorting reverse")
print(sorted(tmp, reverse = True))