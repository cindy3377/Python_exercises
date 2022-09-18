import random
import math
#phase1

def dice_roll():
  return random.randint(1, 6)

while True:
  dice = dice_roll()
  print(f"Dice {dice}")
  if dice == 6:
    break

#phase2

def dice_roll_max(n):
  return random.randint(1, n)

n = int(input("How many sides in your dice?"))

while True:
  dice = dice_roll_max(n)
  print(f"Dice {dice}")
  if dice == n:
    break


#phase3

def gallons_to_liters(gallons):
  return 3.7854 * gallons

while True:
  g = float(input("How many gallons?"))
  if g < 0:
    break
  print(f"{g} gallons are {gallons_to_liters(g):.1f} liters.")

#phase4

def sum(l):
  s = 0
  for e in l:
    s += e
  return s

numberlist = []
for n in range(10):
  numberlist.append(random.randint(1, 10))
print (f"List is: ")
for i in range(len(numberlist)):
  print(numberlist[i], end="")
print(f"\nSum is {sum(numberlist)}")

#phase5

def make_even(l):
  result = []
  for i in range(len(l)):
    if l[i] % 2 == 0:
      result.append(l[i])
  return result

def print_list(prompt, l):
  print(prompt, end=": ")
  for i in range (len(l)):
    print(l[i], end= "")

numberlist = []
for n in range(10):
  numberlist.append(random.randint(1,99))
print_list("Original list", numberlist)
newlist = make_even(numberlist)
print_list("\nModified list", newlist)
print()

#phase6

def pizza_efficient(d, price):
   return price / math.pi * (d/100) ** 2

p1_diameter = float(input("Give the diameter of the first pizza (in cm)?"))
p1_price = float(input("Give the price of the first pizza (in euros)?"))
p2_diameter = float(input("Give the diameter of the second pizza (in cm)?"))
p2_price = float(input("Give the price of the second pizza (in euros)?"))

if pizza_efficient(p1_diameter, p1_price) < pizza_efficient(p2_diameter, p2_price):
  print("First pizza gives better performance")
else:
  print("Second pizza gives better performance.")

