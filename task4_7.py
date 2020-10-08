def fact(n):
    a = 1

    for i in range(1, n+1):
        a = a * i
        yield a

# First method
fact_gen = fact(4)
print(next(fact_gen))
print(next(fact_gen))
print(next(fact_gen))
print(next(fact_gen))


# Second method
for i in fact(4):
    print(i)
