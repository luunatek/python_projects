from itertools import count, cycle


def count_1(var1):
    for i in count(var1):
        if i > 10:
            break
        else:
            print(i)


count_1(4)


def cycle_1(var):
    c = 0
    for i in cycle(var):
        if c > 10:
            break
        print(i)
        c += 1


cycle_1("Hi")

