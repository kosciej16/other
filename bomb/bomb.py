import re

global words

with open('words', 'r') as f:
    global words
    words = re.split(r'\s', f.read())
    del words[-1]


def next_letter(which):
    global words
    possible_letters = raw_input()
    words = [word for word in words if word[which] in possible_letters]
    print (words)

i = 0
while len(words) > 1:
    next_letter(i)
    i += 1
