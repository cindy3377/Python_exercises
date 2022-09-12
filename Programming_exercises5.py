#1 Write a program that asks the user how many dice to roll. The program rolls all the dice once and prints out the the sum of the numbers. Use a for loop.

import random

dice_number = int(input("How many dice to roll?"))
sum = 0
for i in range(dice_number):
        result = random.randint(1,6)
        sum += result
print("Sum of the numbers on the dice", sum)

#2 Write a program that asks the user to enter numbers until they input an empty string to quit. At the end, the program prints out the five greatest numbers sorted in descending order.
# Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.

numbers = []
number = input("Enter the number: ")

while number != "":
        numbers.append(number)
        number = input("Enter the number: ")
dsc_numbers = sorted(numbers, reverse=True)
print(f"The five greatest numbers in descending order are, {dsc_numbers[0:5]}")

#3 Write a program that asks the user for an integer and tells if the number is a prime number. Prime numbers are number that are only divisible by one or the number itself.
#For example, number 13 is a prime number as can only be divided by 1 or 13 so that the result is an integer.
#On the other hand, number 21 for example is not a prime number as it can be also be divided by numbers 3 and 7.

numbers = []
n = int(input("Enter the integer: "))
if n > 1:
        for i in range(2, n):
                if (n % i) == 0:
                        print("The number is not a prime number.")
                        break
        else:
                print("The number is a prime number.")
else:
        print("The number is neither a prime nor composite number.")


#4 Write a program that asks the user to enter the names of five cities one by one
# (use a for loop for reading the names) and stores them into a list structure.
# Finally, the program prints out the names of the cities one by one, one city per line,
# in the same order they were read as input. Use a for loop for asking the names and a for/in loop to iterate through the list.

cities = []
index = 0
while index < 5:
        city = input("Enter the names of cities: ")
        cities.append(city)
        index = index + 1

for city in cities:
        print(city)


