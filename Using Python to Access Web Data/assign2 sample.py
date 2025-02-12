import urllib.request
from bs4 import BeautifulSoup

url = input('Enter - ')
position = 18
repeat = 7

for _ in range(repeat):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[position - 1].get('href', None)
    print(f"Retrieving: {url}")

# Print the last name retrieved
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
print(soup.title.string)