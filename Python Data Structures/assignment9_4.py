fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
counts = dict()
words = list()
for line in fh:
    if line.startswith("From "): 
        words = line.split()
        print(words[1])
        for word in words[1] :
            counts[word] = counts.get(word, 0) + 1
print('The word count of word in para.txt file is: ',counts)

     