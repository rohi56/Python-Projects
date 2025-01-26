#The top 10 most common words
fhand = open('C:\\python\\romeo.txt')
counts = dict()
for line in fhand :
    words = line.split()
    for word in words :
        counts[word] = counts.get(word, 0) + 1


lst= list()
lst = sorted([(v,k) for k,v in counts.items()])

lst = sorted(lst, reverse=True)
for v,k in lst[:10] :
    print(k,v)