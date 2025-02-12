#counting word in web txt file
import urllib.request, urllib.parse, urllib.error
handle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in handle:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
for key, value in counts.items():
    print(key, value)

print((sorted([(v,k) for k,v in counts.items()])))