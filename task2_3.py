# Ask user input for numbers from 1 to 12
try:
    user_input = int(input("Enter number from 1 to 12: "))
except ValueError:
    print("Please enter numeric value.")
    user_input = int(input("Enter number from 1 to 12: "))

# Get using list of items
list_1 = ['spring', 'summer', 'autumn', 'winter']

if user_input >= 3 and user_input <= 5:
    print(list_1[0])
elif user_input >= 6 and user_input <= 8:
    print(list_1[1])
elif user_input >= 9 and user_input <= 11:
    print(list_1[2])
elif user_input == 12 or user_input == 1 or user_input == 2:
    print(list_1[3])

# Get using dictionary
dict_1 = {'spring': [3, 4, 5],
          'summer': [6, 7, 8],
          'autumn': [9, 10, 11],
          'winter': [12, 1, 2]}

list_of_keys = [key
                for key, list_of_values in dict_1.items()
                if user_input in list_of_values]
if list_of_keys:
    print(list_of_keys)

