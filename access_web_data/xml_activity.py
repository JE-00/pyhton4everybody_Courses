import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter location: ")
print('Retrieving', url)
uhand = urllib.request.urlopen(url, context=ctx)

data = uhand.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

counts = tree.findall('.//count')
suma = 0

for count in counts:
    suma += int(count.text)

print("Count:", len(counts))
print("Sum:", suma)
