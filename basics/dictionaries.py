fname = input("Enter file: ")

if len(fname) < 1:
    fname = "clown.txt"
hand = open(fname)

dic = dict()
for line in hand:
    line = line.rstrip()
    words = line.split()
    for word in words:

        dic[word] = dic.get(word, 0) + 1  # idiom: retrieve/create/update counter

        """old_count = dic.get(word, 0)  # if the key isnt found the count is zero
        print(word, "old", old_count)
        new_count = old_count + 1
        dic[word] = new_count

        print(word, "new", new_count)"""
        """print(f"-> {word} {dic.get(word, -99)}")
        if word in dic:
            dic[word] = dic[word] + 1
            #print("# EXISTING #")
        else:
            dic[word] = 1
            #print("*** NEW ***")
        #print(word, dic[word])"""

    largest = -1
    the_word = None
    for key, value in dic.items():
        if value > largest:
            largest = value
            the_word = key

    print("Done", the_word, largest)
