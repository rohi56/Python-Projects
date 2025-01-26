fhandle = open('C:\\python\\names.txt')
count = dict()  # Initialize the dictionary outside the loop
for line in fhandle:
    line = line.strip()
    names = line.split()
    for name in names:
        if name not in count:
            count[name] = 1
        else:
            count[name] = count[name] + 1
print(count)
x = count.get(name, 0)
print('The number of name in count is : ', x)

#Using a get funtion in logic
print('Implementing the same using Get() function:')
ghandle = open('C:\\python\\names.txt')
counts = dict()  # Initialize the dictionary outside the loop
for lne in ghandle:
    lne = lne.strip()
    namess = lne.split()
    for nam in namess:
            counts[nam] = counts.get(nam, 0) + 1
print(counts)
