import re

def regexStrip(text, value = r'\s'):
    stripRegex = re.compile(value)
    return stripRegex.sub('', text)

userString = input('please give me a string to test:')

if userString == '':
    print('ok then')
else:
    print(regexStrip(userString))
