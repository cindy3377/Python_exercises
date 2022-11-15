# part1

class Publication:
  def __init__(self, name):
    self.name = name

  def print_information(self):
    print(f"{self.name}")


class Book(Publication):

  def __init__(self, name, author, page_count):
    self.author = author
    self.page_count = page_count
    super().__init__(name)

  def print_information(self):
    print(f"{self.name}: {self.author}, {self.page_count}")


class Magazine(Publication):

  def __init__(self, name, editor):
    self.editor = editor
    super().__init__(name)

  def print_information(self):
    print(f"{self.name}: {self.editor}")


book = Book("Compartment No. 6", "Rosa Liksom", 192)
magazine = Magazine("Donald Duck", "Aki Hyyppä")

book.print_information()
magazine.print_information()

# part2

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


class Race:
  def __init__(self, name, distance, cars_list):
    self.name = name
    self.distance = distance
    self.cars_list = cars_list

  def hour_passes(self):
    for car in self.cars_list:
      car.accelerate(random.randint(-10, 15))
      car.drive(1)

  def print_status(self):
    print(self.name + ":")
    print("Plate  Speed  Travelled distance")
    print("-------------------------------")
    for car in self.cars_list:
      print(f"{car.reg_num:6s}: {car.current_speed:3d}, {car.travdis} km.")

  def race_finished(self):
    for car in self.cars_list:
      if car.travdis >= self.distance:
        return True
    return False


class ElectricCar(Car):
  def __init__(self, reg_num, max_speed, battery):
    self.battery = battery
    super().__init__(reg_num, max_speed)

  def print_info(self):
    print(
      f"Registration number of the electric car: {self.reg_num:6s}, Current speed: {self.current_speed:3d} km/h, Travelled distance: {self.travdis} km.")


class GasolineCar(Car):
  def __init__(self, reg_num, max_speed, volume):
    self.volume = volume
    super().__init__(reg_num, max_speed)

  def print_info(self):
    print(
      f"Registration number of the gasoline car: {self.reg_num:6s}, Current speed: {self.current_speed:3d} km/h, Travelled distance: {self.travdis} km.")


electric_car = ElectricCar("ABC-15", 180, 52.5)

gasoline_car = GasolineCar("ACD-123", 165, 32.3)

electric_car.accelerate(60)
gasoline_car.accelerate(70)

electric_car.drive(1)
gasoline_car.drive(1)

electric_car.accelerate(20)
gasoline_car.accelerate(15)

electric_car.drive(2)
gasoline_car.drive(2)

electric_car.accelerate(30)
gasoline_car.accelerate(20)

electric_car.drive(3)
gasoline_car.drive(3)

electric_car.print_info()
gasoline_car.print_info()
