import re
handle = open("C:\\python\\mbox-short.txt")

for lin in handle:
    lin = lin.rstrip()
    if re.findall('@([^ ]*)', lin):
       x = re.findall('@([^ ]*)', lin)  
       print(x)
