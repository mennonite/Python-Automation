#! python3
# madLibs.py - opens and reads a text file and lets the user input their own words

import re

# open text file
madlibFile = open('.\\Chapter 8 -- Reading and Writing Files\\Practice Projects\\test.txt')

# save the content of the file into a variable
content = madlibFile.read()
madlibFile.close()

# build a regex to identify replaceable words
madlibsRegex = re.compile(r'(ADJECTIVE|NOUN|ADVERB|VERB)')
matches = madlibsRegex.findall(content)

# for each match, prompt the user to replace it
for match in matches:
    userWord = input('Gimme %s %s:\n' %('an' if match.startswith('A') else 'a', match.lower()))
    content = content.replace(match, userWord, 1)

print(content)

# the resulting text is saved to a new file
madlibAnswers = open('.\\Chapter 8 -- Reading and Writing Files\\Practice Projects\\test-answer.txt', 'w')
madlibAnswers.write(content)
madlibAnswers.close()