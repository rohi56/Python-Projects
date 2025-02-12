#Using re.search() line find()

print("Using find() :")
hand = open('C:\\python\\mbox-short.txt')
for line in hand :
    line = line.rstrip()
    if line.find('From: ') >= 0 :
        print(line)

print("\n\n\nUsing re.search() :")
import re
hand = open('C:\\python\\mbox-short.txt')
for line in hand :
    line = line.rstrip()
    if re.search('From: ', line) :
        print(line)

