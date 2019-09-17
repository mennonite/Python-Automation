spam = ['apples', 'bananas', 'tofu', 'cats']

def shit(list):
    x = ''
    if list == []:
        return x
    else:
        for i in range(len(list)-1):
            x = x + list[i] + ', '
        x = x + 'and ' + list[-1]
        return x

print(shit(spam))