#python!
#walk.py - an example program that showcases the os.walk() function

import os

for folderName, subfolders, filenames in os.walk('..\\..\\nuts'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')