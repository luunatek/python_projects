# Define empty variable and list
total = 0
user_input = []

while True:
    user_input = input("Enter numbers or 'stop' to exit program : ")
    number = user_input.split()
    try:
        for i in number:
            total = total + int(i)
        print(total)
    except (TypeError, ValueError):
        if user_input.lower() == 'stop':
            break
        else:
            print("Please enter number.")
            continue
