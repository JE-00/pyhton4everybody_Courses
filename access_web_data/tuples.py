fname = input("Enter file: ")
if len(fname) < 1:
    fname = "clown.txt"
hand = open(fname)

dic = dict()
for line in hand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        # idiom: retrieve/create/update counter
        dic[word] = dic.get(word, 0) + 1

# print(dic)

temp = list()
for key, value in dic.items():
    newt = (value, key)
    temp.append(newt)
# print("Flipped", temp)

temp = sorted(temp, reverse=True)
# print("Sorted", temp[:5])

for value, key in temp[:5]:
    print(key, value)

print("-" * 50)

# Lo mismo resumido
print(sorted([(value, key) for key, value in dic.items()], reverse=True)[:5])
