number = int(input("Enter number: "))

max_number = 0
rem = 0

while number != 0:
    rem = number % 10
    if rem > max_number:
        max_number = rem
    number = number // 10

print(max_number)

