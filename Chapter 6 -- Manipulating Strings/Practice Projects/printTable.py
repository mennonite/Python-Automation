def printTable(list):
    colWidths = [0] * len(list)
    for x in range(len(list)):
        colWidths[x] = len(max(list[x], key=len))

    for i in range(len(list[0])):
        for j in range(len(list)):
            print(list[j][i].rjust(colWidths[j]), end=' ')
        print()
    
    return list

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)