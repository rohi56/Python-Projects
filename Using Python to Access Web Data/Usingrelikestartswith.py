#Using re.search() line startswith()

print("Using find() :")
hand = open('C:\\python\\mbox-short.txt')
for line in hand :
    line = line.rstrip()
    if line.startswith('From: ') :
        print(line)

print("\n\n\nUsing re.search() :")
import re
hand = open('C:\\python\\mbox-short.txt')
for line in hand :
    line = line.rstrip()
    if re.search('^From: ', line) :
        print(line)