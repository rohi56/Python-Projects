# Using API proxy from opengeo
import urllib.request, urllib.parse, urllib.error
import json
import ssl

serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter your location: ')
    if len(address) < 1: break

    address = address.strip()
    parms = dict()
    parms['q'] = address

    url = serviceurl + urllib.parse.urlencode(parms)
    
    print('Retrieving:', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'features' not in js :
        print('==== Download Error ====')
        print(data)
        break
    
    if len(js['features']) == 0:
        print('==== Object not Found ====')
        print(data)
        continue

    #print(json.dumps(js, indent=4))

    lat = js['features'][0]['properties']['lat']
    lon = js['features'][0]['properties']['lon']
    location = js['features'][0]['properties']['formatted']

    print('Latitude:', lat)
    print('Longitude:', lon)
    print('Location:', location)