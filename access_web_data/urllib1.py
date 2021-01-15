import urllib.request
import urllib.parse
import urllib.error

# Lee el contenido de la página (Headers)
fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

# Lee el código de la página (Response)
fhand2 = urllib.request.urlopen("http://dr-chuck.com/page1.htm")
for line in fhand2:
    print(line.decode().strip())
