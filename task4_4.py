ll = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(f'Current list: {ll}')

new_List = [x for x in ll if ll.count(x) == 1]

print(f'Unique items in the list: {new_List}')
