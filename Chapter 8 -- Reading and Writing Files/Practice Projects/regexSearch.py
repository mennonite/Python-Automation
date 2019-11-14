#! python3
# regexSearch.py - a program that opens all .txt files in a folder and searches for a LINE that matches a user-supplied regular expression and prints that LINE to the screen                  

import os, re

# opens a folder and adds all items to a list
files = os.listdir(os.path.join(os.getcwd(), 'Chapter 8 -- Reading and Writing Files', 'Practice Projects'))

# create a regex to find all text files
textRegex = re.compile(r'.txt$')

# use the regex to add the text files to a list
textFiles = []
for item in files:
    if textRegex.search(item) is not None:
        textFiles.append(item)

# ask user for a regular expression
userRegexString = input('Please input a regular expression you would like to search for:\n')

userRegex = re.compile(userRegexString)                                                 # pray to Christ the user knows what a regular expression is

# run the regex against the text files and print the matches (if any) to the screen
count = 0
indexPrinted = []

for item in textFiles:
    # copies text file content to a variable
    testFile = open(os.path.join(os.getcwd(), 'Chapter 8 -- Reading and Writing Files', 'Practice Projects', item))
    content = re.split(r'\n|\.', testFile.read())                                       # separates the text from the file into lines using a newline or period as the delimiter
    testFile.close()
    print('Now searching %s for %s:' % (item, userRegexString))
    while count < len(content):
        content[count] = content[count].strip()
        matches = userRegex.findall(content[count])
        if matches != [] and str(count) not in indexPrinted:
            for match in matches:
                content[count] = content[count].replace(match, match.upper(), 1)       # capitalizes all the matches for legibility         
            print(content[count])                                                      # will only print a line once even if it contains more than one match                                         
            indexPrinted.append(str(count))                                            
            count += 1
        else:
            count += 1
    if indexPrinted == []:
        print('No matches found!')
    print()
    count = 0                                                                          # resets the count for the next file
    indexPrinted.clear()                                                               # clears the list for the next file
