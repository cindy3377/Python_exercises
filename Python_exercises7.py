#1 Write a program that asks the user for a number of a month and then prints out the corresponding season
# (spring, summer, autumn, winter). Save the seasons as strings into a tuple in your program. We can define
# each season to last three months, December being the first month of winter.


months_of_the_year = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
month_number = int(input("Enter the month number (1-12): "))
month = months_of_the_year[month_number-1]

if month in months_of_the_year[0:2]:
    season = "Winter"
elif month in months_of_the_year[11]:
    season = "Winter"
elif month in months_of_the_year[2:5]:
    season = "Spring"
elif month in months_of_the_year[5:8]:
    season = "Summer"
else:
    season = "Autumn"

print(season)


#2 Write a program that asks the user to enter names until he/she enters an empty string.
# After each name is read the program either prints out New name or Existing name depending on
# whether the name was entered for the first time. Finally, the program lists out the input names one by one,
# one below another in any order. Use the set data structure to store the names.

name = input("Enter the name: ")
names = set()
while name != "":
    if name in names:
        print("Already existing:", name)
    else:
        print("New name:", name)
    names.add(name)
    name = input("Enter the name: ")

for name in names:
    print(name)

#3 Write a program for fetching and storing airport data. The program asks the user if they want to enter a new airport,
# fetch the information of an existing airport or quit. If the user chooses to enter a new airport, the program asks
# the user to enter the ICAO code and name of the airport. If the user chooses to fetch airport information instead,
# the program asks for the ICAO code of the airport and prints out the corresponding name. If the user chooses to quit,
# the program execution ends. The user can choose a new option as many times they want until they choose to quit.
# (The ICAO code is an identifier that is unique to each airport. For example, the ICAO code of Helsinki-Vantaa Airport is EFHK.
# You can easily find the ICAO codes of different airports online.)


airport = {}

print("What would you like to do?")
print("Press 1 to enter a new airport")
print("Press 2 to fetch the information of an existing airport")
print("Press 3 to quit the program")
input = int(input("Press a number:"))


while action == 1 or action == 2:
  if action == 1:
    new_ICAO = input("Add new ICAO code:")
    new_name = input("Add new airport name: ")
    airport.update({new_ICAO:new_name})
    print(airport)
    action = int(input("Press a number:"))
  else:
    existing_ICAO = input("Fetch airport: ")
    if existing_ICAO in airport:
      print(airport.get(existing_ICAO))
      print("Already exist!")
      action = int(input("Press a number:"))

    else:
      print("Not exist!")
      action = int(input("Press a number:"))
print("Program ends!")
