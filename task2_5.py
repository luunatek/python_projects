rating = int(input("Enter new rating item: "))

my_list = [7, 5, 3, 3, 2]
my_list.append(rating)

my_list = sorted(my_list)
my_list = my_list[::-1]
print(f'User entered number {rating}. Result: {my_list}')
