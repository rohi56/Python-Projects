# Reading a HTM file
import urllib.request, urllib.parse, urllib.error
import re

handle = urllib.request.urlopen('http://dr-chuck.com/page1.htm')
for line in handle:
    line = line.decode().strip()
    urls = re.findall('href="(http://.*?)"', line)
    for url in urls:
        print(url)