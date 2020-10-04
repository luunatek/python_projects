num_1 = input("Enter first number: ")
num_2 = input("Enter second number: ")


def divide_number(num_1, num_2):
    try:
        result = int(num_1) // int(num_2)
        print(result)
    except ZeroDivisionError:
        print("You cannot divide number by 0.")
    except ValueError:
        print("You can only enter numbers.")


divide_number(num_1, num_2)

