'''
Aggregation: It's a concept in obeject oriented programming which involves the process of creating an object of one class in another class.
Aggregation is used when there exists a "has-a" relationship.
We'll have two scenarioss in aggregation:
  Scenario 1: Create object in main space and use in current class.
    Advantage: This object can be used by multiple classes.
    Disadvantage(negligible): It can lead memory wastage if it's not being used by other classes.
  Scenario 2: Create and use in current class.
    Advantage: Herein, the objects are dynamic.
    Disadvantage: Objects are limited to the current class only.
'''

# Scenario 02: Create and use object in current class.

'''
We've two classes: Car and Driver.
  Car:
    Properties: Car Model, Car Color, Car Brand
    Functionalities: Start, Accelerate, Stop.
  Driver:
    Properties: Driver Name, Driver Age, Driver Expeerience, [Driver Car]
    Functionalites: Driving
'''

class Car:
  def __init__(self, cm, cc, cb):
    self.car_model = cm
    self.car_color = cc
    self.car_brand = cb
  def start(self):
    print(f'{self.car_model} Has Started!')
  def accelerate(self):
    print(f'{self.car_model} Is Accelerating!')
  def stop(self):
    print(f'{self.car_model} Has Stopped!')

class Driver:
  def __init__(self, dn, da, dex):
    self.driver_name = dn
    self.driver_age = da
    self.driver_experience = dex

    #Herein, we'll take input for creating a car object.
    cm = input('Enter Car Model: ')
    cc = input('Enter Car Color: ')
    cb = input('Enter Car Brand: ')
    car_object = Car(cm, cc, cb)

    # Herein, we're defining driver car property and we're assigning it the object of car class as a value.
    self.driver_car = car_object

  def driving(self):
    print(f'{self.driver_name} Has Entered His {self.driver_car.car_model} Car!')
    self.driver_car.start()
    self.driver_car.accelerate()
    self.driver_car.stop()
    print(f'{self.driver_name} Has Exited His {self.driver_car.car_model} Car!')