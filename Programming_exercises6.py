# FUNCTIONS

#1 Write a function that returns a random dice roll between 1 and 6.
# The function should not have any parameters.
# Write a main program that rolls the dice until the result is 6.
# The main program should print out the result of each roll.

import random

def random_dice():
    result = random.randint(1, 6)
    return result
def main():
    result = random_dice()
    while result != 6:
        print("The random result is:", result)
        result = random_dice()
    print("The result is 6")

main()

#2 Modify the function above so that it gets the number of sides on the dice as a parameter.
# With the modified function you can for example roll a 21-sided role-playing dice.
# The difference to the last exercise is that the dice rolling in the main program continues
# until the program gets the maximum number on the dice, which is asked from the user at the beginning.

dice = int(input("Maximum number on dice: "))

def modified_random_dice(dice):
    result = random.randint(1, dice)
    return result

def modified_main():
    result = modified_random_dice(dice)
    while result < dice:
        print("The random result is:", result)
        result = modified_random_dice(dice)
    print("The maximum result is", dice)

modified_main()

#3 Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres.
# Write a main program that asks for a volume in gallons from the user and converts the value to liters.
# The conversion must be done by using the function. Conversions continue until the user inputs a negative value.


def gallon_to_liter(gallons):
    liters = 3.78541 * gallons
    return liters

def main():
    volume_gallons = float(input("Volume in gallons:"))
    while volume_gallons >= 0:
        liter = gallon_to_liter(volume_gallons)
        print(f"Conversion from {volume_gallons:.1f} volume in gallons to volume in liters is: {liter:.1f}.")
        volume_gallons = float(input("Volume in gallons:"))
main()

#4 Write a function that gets a list of integers as a parameter.
# The function returns the sum of all the numbers in the list.
# For testing, write a main program where you create a list,
# call the function, and print out the value it returned.

def sum_of_integers(list):
    list_sum = sum(list)
    return list_sum

def main():

    list_integers = [1, 2, 4, 6, 7]
    list_sum = sum_of_integers(list_integers)
    print("Sum of all the numbers in the list:", list_sum)

main()


#5 Write a function that gets a list of integers as a parameter.
# The function returns a second list that is otherwise the same as the original list
# except that all uneven numbers have been removed. For testing, write a main program
# where you create a list, call the function, and then print out both the original
# as well as the cut-down list.
list = [1, 2, 4, 6, 7, 9, 11, 12]


def list_of_integers(list):
    modified_list = []
    for elem in list:
        if elem % 2 != 0:
            modified_list.append(elem)
    return modified_list


def main():
    list = [1, 2, 4, 6, 7, 9, 11, 12]
    modified_list = list_of_integers(list)
    print("original", list)
    print("modified", modified_list)


main()


#6 Write a function that receives two parameters: the diameter of a round pizza in centimeters and the price of the pizza in euros.
# The function calculates and returns the unit price of the pizza per square meter.
# The main program asks the user to enter the diameter and price of two pizzas and tells the user which pizza provides better value for money
# (which of them has a lower unit price). You must use the function you wrote for calculating the unit prices.

import math

def cal_unit_price (diameter, price):
    radius = (diameter/2)*0.01
    area = math.pi*(radius ** 2)
    result = price/area
    return result

d1 = float(input("Enter the diameter of the pizza 1: "))
p1 = float(input("Enter the price of the pizza 1: "))
d2 = float(input("Enter the diameter of the pizza 2: "))
p2 = float(input("Enter the price of the pizza 2: "))

unit_price_pizza_1 = cal_unit_price(d1, p1)
unit_price_pizza_2 = cal_unit_price(d2, p2)
print("Pizza 1: ", unit_price_pizza_1)
print("Pizza 2: ", unit_price_pizza_2)

if unit_price_pizza_1 > unit_price_pizza_2:
    print("Pizza 1 is more expensive than pizza 2")
elif unit_price_pizza_2 > unit_price_pizza_1:
    print("Pizza 2 is more expensive than pizza 1")
else:
    print("Pizza 1 and pizza 2 have the same price per value")








