import urllib.request,  urllib.error, urllib.parse
import json
handle = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_42.json')
data = handle.read()
info = json.loads(data)
sum = 0
for item in info['comments']:
    sum += item['count']
print(sum)
