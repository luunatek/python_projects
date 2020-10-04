# First method
def my_func(x, y):
    return x ** y


print(my_func(3, 2))


# Second method
def my_func(x, y):
    while y > 0:
        return pow(x, y)


print(my_func(4, 2))
