import random
class Car:
  def __init__(self, reg_num, max_speed):
    self.reg_num = reg_num
    self.max_speed = max_speed
    self.current_speed = 0
    self.travdis = 0
  def accelerate(self, change_speed):
    self.current_speed = min(max(self.current_speed + change_speed, 0), self.max_speed)

  def drive(self, time):
    self.travdis += self.current_speed * time

tesla = Car("ABC-123", 142)

#part1
print(f"Car registration number is {tesla.reg_num}, its max speed is {tesla.max_speed} km/h, current speed is {tesla.current_speed} km/h, travelled distance is {tesla.travdis} km")

#part2
tesla.accelerate(30)
print(f"Current speed: {tesla.current_speed} km/h")
tesla.accelerate(70)
print(f"Current speed: {tesla.current_speed} km/h")
tesla.accelerate(50)
print(f"Current speed: {tesla.current_speed} km/h")
tesla.accelerate(-200)
print(f"Current speed: {tesla.current_speed} km/h")

#part3
tesla.accelerate(60)
tesla.drive(1.5)
print(f"Distance travelled: {tesla.travdis} km.")

#part4
car_list = []
for i in range(10):
  car_list.append(Car("ABC-"+ str(i+1), random.randint(100, 200)))

travMax = 0
while travMax < 10000:
  for car in car_list:
    car.accelerate(random.randint(-10, 15))
    car.drive(1)
    travMax = max(car.travdis, travMax)
for car in car_list:
  print(f"{car.reg_num}:6s : {car.max_speed}, {car.travdis}")

print(f"The winner was able to travel: {travMax}")


