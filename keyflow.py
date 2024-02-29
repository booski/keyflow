#!/usr/bin/env python3

import fileinput
import sys

def checkWord(word, progression):
    remaining = progression
    for letter in word:
        index = remaining.find(letter)
        if index == -1:
            break
        # exclude the found letter
        index += 1
        remaining = remaining[index:]
    else:
        print(word)
    
def wordGenerator():
        for line in fileinput.input(files=(sys.argv[1:])):
            for word in line.split():
                yield word

if __name__ == '__main__':
    progression = 'qazwsxedcrfvtgbyhnujmikolpöåä'

    words = wordGenerator()
    try:
        while True:
            checkWord(next(words), progression)
    except StopIteration:
        exit(0)
