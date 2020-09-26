a = int(input("Enter first day running in km: "))
b = int(input("Enter goal in km: "))

day = []
while a < b:
    a = a + (a * 0.1)
    day.append(a)

new_list = ['%.2f' % elem for elem in day]
for count, item in enumerate(new_list):
    print('Day',count+1,':', item)

print('On day', count+1, 'athlete reached his goal by running', b,'km.')
