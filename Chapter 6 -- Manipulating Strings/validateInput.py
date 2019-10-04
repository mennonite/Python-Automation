while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('\nPlease enter a number for your age.\n')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('\nPasswords can only have letters and numbers.\n')