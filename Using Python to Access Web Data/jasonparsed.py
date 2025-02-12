import json

data = '''
{
    "users": [
        {
            "status": {
                "text": "Just posted a photo"
            },
            "location": "San Francisco, California",
            "screen_name": "leahculver",
            "name": "Leah Culver"
        },
        {
            "status": {
                "text": "Enjoying the sunny weather"
            },
            "location": "New York, New York",
            "screen_name": "johnsmith",
            "name": "John Smith"
        }
    ]
}
'''

info = json.loads(data)
print('User count:', len(info['users']))
for item in info['users']:
    print('Name:', item['name'])
    print('Screen name:', item['screen_name'])
    print('Location:', item['location'])
    print('Status:', item['status']['text'])