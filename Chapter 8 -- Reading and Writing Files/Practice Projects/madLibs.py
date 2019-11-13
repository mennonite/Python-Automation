#! python3
# madLibs.py - opens and reads a text file and lets the user input their own words

import re

# open text file
madlibFile = open('.\\Chapter 8 -- Reading and Writing Files\\Practice Projects\\test.txt')

# save the content of the file into a variable

content = madlibFile.read().split()
madlibFile.close()
searchList = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']

for i in range(len(content)):
    # prompt the user to enter a [searched term] of their choice if [searched term] exists in text file
    if content[i].strip('.') in searchList:
        if content[i].startswith('A') and content[i].endswith('.'):
            content[i] = input('Gimme an %s:\n' % content[i].strip('.').lower()) + '.'
        elif content[i].startswith('A'):
            content[i] = input('Gimme an %s:\n' % content[i].lower())
        elif content[i].endswith('.'):
            content[i] = input('Gimme a %s:\n' % content[i].strip('.').lower()) + '.'
        else:
            content[i] = input('Gimme a %s:\n' % content[i].lower())

print(' '.join(content))


# TODO: the resulting text is saved as a new file