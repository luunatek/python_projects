# Convert seconds
seconds_in_day = 86400
seconds_in_hour = 3600
seconds_in_minute = 60
minutes_in_hour = 60

while True:
    seconds = input("Please enter time in seconds: ")
    if seconds.isalpha():
        print("Please enter only numbers!")
    elif int(seconds) <= 0:
        print("Please enter positive number.")
    elif int(seconds) > seconds_in_day:
        print(f"The number is too big. Please enter number not bigger then {seconds_in_day}")
    else:
        hour = int(seconds) // seconds_in_hour
        minutes = (int(seconds) % seconds_in_hour) // minutes_in_hour
        seconds = (int(seconds) % seconds_in_hour) % seconds_in_minute
        print(f'{hour}:{minutes}:{seconds}')
        break
