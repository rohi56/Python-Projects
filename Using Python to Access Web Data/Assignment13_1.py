#Assignment 13
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
handle = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_42.xml')
data = handle.read()
tree = ET.fromstring(data)
counts = tree.findall('.//count')
sum = 0
for count in counts:
    sum += int(count.text)
print(sum)
