import re

def regexStrip(text, value = r''):
    if value == '':
        stripRegex = re.compile(r'^(\s*)(.*)(\s)*$')
        trim = stripRegex.search(text)
        return trim.group(2)
    else:
        stripRegex = re.compile(value)
        return stripRegex.sub('', text)

userString = input('Please give me a string to test:')

if userString == '':
    print('ok then')
else:
    char = input('Please input a character you would like to remove from your string.\n(If left blank it will remove spaces from the beginning and end of the string):\n')
    print(regexStrip(userString, char))
