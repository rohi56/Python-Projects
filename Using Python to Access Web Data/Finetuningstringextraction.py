#Fine tuning string extraction
import re
handle = open("C:\\python\\mbox-short.txt")
for line in handle:
    line = line.rstrip()
    if re.findall('^From (\S+@\S+)', line):
       y = re.findall('\S+@\S+', line)  
       print(y)

