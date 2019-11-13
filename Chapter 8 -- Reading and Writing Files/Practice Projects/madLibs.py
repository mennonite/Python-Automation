#! python3
# madLibs.py - opens and reads a text file and lets the user input their own words

# TODO: search a text file for a word from the following list: [ADJECTIVE, NOUN, ADVERB, VERB]

# open txt file
madlibFile = open('test.txt')

# save the content of the file into a variable

content = madlibFile.read()
madlibFile.close()

searchList = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
for word in searchList:
    for i in content.split():
        if i.upper() == word and word == 'ADJECTIVE':
            i = input('Enter an adjective:')
            print(i)
        elif i.upper() == word:
            i = input('Enter a %s:' % word)
            print(i)


# TODO: prompt the user to enter a [searched term] of their choice

# TODO: the users term replaces the listed word in the text file and prints it to the screen

# TODO: the resulting text is saved as a new file