#phase 1
name = input("what is your name?")

print("Hello, " + name +"!")

#phase 2

radius = float(input("Give the radius?"))
print(f"Area is {math.pi * radius ** 2:.1f}")

#phase 3

length = input("The length of the rectangle: ")
width = input("The width of the rectangle: ")
length_str = float(length)
width_str = float(width)

area = length_str*2 + width_str*2
print(f"Area is {area:.1f}")

perimeter = length_str*width_str

print(f"Perimeter is {perimeter:.1f}")


#phase 4

num1 = input("Put in the first number: ")
num2 = input("Put in the second number: ")
num3 = input("Put in the third number: ")

num1_str = float(num1)
num2_str = float(num2)
num3_str = float(num3)

sum = num1_str + num2_str + num3_str

print(f"Sum of the three numbers is: {sum:.0f}")

product = num1_str*num2_str*num3_str

print(f"Product of the three numbers is: {product:.0f}")

average = (num1_str + num2_str + num3_str)/3

print(f"Average of the three number is: {average:.0f}")


#phase 5


talent = float(input("Put in the talent: "))
pound = float(input("Put in the pound: "))
lot = float(input("Put in the lot: "))
totalGram = (lot + 32*pound + 32*20*talent) *13.3

kilogram = totalGram // 1000

gram =totalGram % 1000

print(f"The weight in modern units: {kilogram:1.0f} kilograms and {gram:.2f} grams")


#phase 6

print(f"{random.randint(0, 999):03d}")
print(str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)))

print(f"{random.randint(1, 6666):04d}")
print(str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)))


