
# the simplest way to work wih a file!
fp = open("text.txt")
print(fp.read())
fp.close()

fp = open("text.txt")

# files are iterable
for line in fp:
    # print(line, end="")
    # print(line[:-1])
    print(line.rstrip())

import requests
r = requests.get("https://www.gutenberg.org/cache/epub/345/pg345.txt")
fp = open('dracula.txt', 'w')
fp.write(r.text)






