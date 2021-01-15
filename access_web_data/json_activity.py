"""
Activity 1 JSON
"""
import urllib.request, urllib.parse, urllib.error
import json
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

info = json.loads(data)

suma = 0
count = 0

for comment in info['comments']:
    suma += comment['count']
    count += 1

print("Count:", count)
print("Sum:", suma)
