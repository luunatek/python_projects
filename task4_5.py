from functools import reduce
ll = [i for i in range(100, 1001) if i % 2 == 0]
#print(ll)
new_list = reduce( (lambda x,y: x*y), ll)
print(new_list)
