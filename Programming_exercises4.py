#1Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.

n = 1
while n <= 1001:
    if n%3 == 0:
        print(str(n))
    n = n + 2



#2Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.


inches = float(input("Put in the centimeters: "))

while inches >= 0:
    centimeters = inches * 2.54
    print(f"Value in centimeters is {centimeters:.2f}")
    inches = float(input("Put in the centimeters: "))
print("Program ends")


#3Write a program that asks the user to enter numbers until they enter an empty string to quit. Finally, the program prints out the smallest and largest number from the numbers it received.

number = input ("Enter number: ")
temp = float(number)
largest_number = temp
smallest_number = temp
while number!="":
    temp = float(number)
    if largest_number < temp:
        largest_number = temp
    elif temp < smallest_number:
        smallest_number = temp
    number = input("Enter number: ")
print ("Largest number: ",largest_number)
print ("Smallest number: ", smallest_number)



#4Write a game where the computer draws a random integer between 1 and 10. The user tries to guess the number until they guess the right number. After each guess the program prints out a text: Too high, Too low or Correct. Notice that the computer must not change the number between guesses.

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




#5Write a program that asks the user for a username and password. If either or both are incorrect, the program ask the user to enter the username and password again.
# This continues until the login information is correct or wrong credentials have been entered five times.
# If the information is correct, the program prints out Welcome. After five failed attempts the program prints out Access denied. The correct username is python and password rules.

correct_username = "python"
correct_password = "rules"
username = input("Enter your username:")
password = input("Enter your password:")

submit_times = 0

while submit_times < 4:
    if username != correct_username or password != correct_password:
        print("Wrong! Enter again username and password:")
        username = input("Enter your username:")
        password = input("Enter your password:")
        submit_times = submit_times + 1

    elif username == correct_username and password == correct_password:
        print("Welcome!")
        break

if submit_times >= 4:
    print("You've exceeded 5 times. Access denied!")





#6

import random

N = int(input("Generate the number of random points: "))
count = 0
n = 0

while count < N:
    x = float(random.uniform(-1, 1))
    y = float(random.uniform(-1, 1))
    if x**2 + y**2 < 1:
        n = n + 1
    count = count + 1

pi = float((4*n)/N)

print(f"The approximation of pi is: {pi:.3f}")



### Input number N
### declare count = 0
### declare pi = 0


### declare n = 0


### while loop count < N ?
#### generate coordinate of point (x, y) within [-1, 1]
#### compare if point within circle (using x^2 + y^2 < 1)
#### if true n++
#### count++

### pi = 4*n / N
