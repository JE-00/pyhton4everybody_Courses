import re

# one liner con list comprehension
print(sum([int(n) for n in re.findall('[0-9]+', open("regex_sum_1126455.txt").read())]))
"""
fname = "regex_sum_1126455.txt"
hand = open(fname)

numlist = list()
for line in hand:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)

    for number in numbers:
        num = int(number)
        numlist.append(num)

print("Sum: ", sum(numlist))
"""
# Sum:  428924
