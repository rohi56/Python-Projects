#Using a get funtion in logic
fhandle = open('C:\\python\\para.txt')
counts = dict()  # Initialize the dictionary outside the loop
for line in fhandle:
    line = line.strip()
    words = line.split()
    for word in words:
            counts[word] = counts.get(word, 0) + 1
print('The word count of word in para.txt file is: ',counts)

print('Using definite loops and dictionaries')
for key in counts :
      print(key, ':', counts[key])

print('Retriving list of key and values')
print('the list of words :', list(counts))
print('the list of words in counts : ',(list(counts.keys())))
print('the value of words in counts : ',(list(counts.values())))
print('the items of words in counts : ',(list(counts.items())))

print('Two - iteration variable:')
for aaa,bbb in counts.items() :
      print(aaa, ':',bbb)