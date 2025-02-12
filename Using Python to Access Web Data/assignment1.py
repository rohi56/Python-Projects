import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the span tags
count = 0
tags = soup('span')
for tag in tags:
    count += int(tag.text)
print(count)
   