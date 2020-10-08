my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(my_list)

new_list = [el for id, el in enumerate(my_list) if my_list[id-1] < my_list[id]]

print(new_list[1:])
