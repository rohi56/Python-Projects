#Spam Confidence
import re
handle = open("C:\\python\\mbox-short.txt")
numlist = list()
for line in handle:
    line = line.rstrip()
    x = re.findall("^X-DSPAM-Confidence: ([0-9.]+)", line)
    if len(x) > 0:
        num = float(x[0])
        numlist.append(num)
print("Maximum:", max(numlist))