#Assignment 13_2
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
handle = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_2131494.xml')
data = handle.read()
tree = ET.fromstring(data)
counts = tree.findall('.//count')
sum = 0
for count in counts:
    sum += int(count.text)
print(sum) 