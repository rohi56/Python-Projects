import urllib.request,  urllib.error, urllib.parse
import json
handle = urllib.request.urlopen('https://py4e-data.dr-chuck.net/comments_2131495.json')
data = handle.read()
info = json.loads(data)
sum = 0
for item in info['comments']:
    sum += item['count']
print(sum)
