def my_func(*var):
    new_list = []
    for i in var:
        new_list.append(i)
        new_list.sort()
    return new_list[-1] + new_list[-2]


print(my_func(7, 2, 3))
