
"""
answer = float(input("The length of a zander in centimeters: "))
actual_size = float(answer)
cutdown_size = 42 - actual_size
if answer < 42:
    print(f"Release the fish back to the lake, the fish is {cutdown_size:.1f}" +
          " centimeters below the size limit")
else:
    print("Nice fishing time!")





cabin_class = input("Enter the cabin class of the cruise ship:")
if cabin_class == "LUX":
    print("upper-deck cabin with a balcony")
elif cabin_class == "A":
    print("above the car deck, equipped with a window")
elif cabin_class == "B":
    print("windowless cabin above the car deck")
elif cabin_class == "C":
    print("windowless cabin below the car deck")
else:
    print("Invalid cabin class")







gender = input("Enter your biological gender:")
hemoglobin_value = input("Enter your hemoglobin value (g/l):")

if gender != "female" and gender != "male":
    print('Gender unknown')
    exit()

try:
    hemo_int = int(hemoglobin_value)
except:
    print('Wrong input of hemoglobin value')
    exit()

hemo_int = int(hemoglobin_value)

if gender == "female":
    if hemo_int < 117:
        print("The hemoglobin level is low")
    elif hemo_int > 155:
        print("The hemoglobin level is high")
    else:
        print("You have normal hemoglobin level")
elif gender == "male":
    if hemo_int < 134:
        print("The hemoglobin level is low")
    elif hemo_int > 167:
        print("The hemoglobin level is high")
    else:
        print("You have normal hemoglobin level")








year_input = float(input("Enter the year:"))

if year_input % 4 == 0 and year_input % 100 != 0 or year_input % 400 == 0:
    print("It is a leap year.")
else:
    print("It is NOT a leap year.")

"""

import random


random_number = random.randint(1,10)
random_guess = int(input("Enter the number you guess: "))

while random_guess != random_number:
    if random_guess > random_number:
        print("Too high")
        random_guess = int(input("Enter the number you guess: "))
    else:
        print("Too low")
        random_guess = int(input("Enter the number you guess: "))
print ("Correct, number is", random_number)
