import re

def isStrongPassword(text):
    #create a regex pattern for character length
    lengthRegex = re.compile(r'.{8,}')

    #create a second (and third) regex pattern for presence of both upper and lowercase characters
    smallRegex = re.compile(r'[a-z]')
    bigRegex = re.compile(r'[A-Z]')

    #create a fourth regex pattern for presence of at least one digit
    numRegex = re.compile(r'\d')

    if lengthRegex.search(text) != None:
        if smallRegex.search(text) != None:
            if bigRegex.search(text) != None:
                if numRegex.search(text) != None:
                    return True
    else:
        return False

while True:
    print('Please input a password below: \n')
    password = input()
    if isStrongPassword(password):
        print('''
        You
        Have broken the loop
        Yes
        YES
        You are free
        ''')
        break
    else:
        print('Try again.\n')