"""import datetime
# Class = Structure of an object. Classes can have attributes. Classes can have methods (functions inside the class).
# Object = Used to store data. Created from a class. A variable where the data is saved and the methods define or change its data. Objects can be used in modules.
class Player:
    def do_something(self):
        pass

word = "hello"
word.capitalize()
player1 = Player()
player1.do_something()

datetime.datetime().date"""
# Program where a Person drives a Car.

class Person:
    def __init__(self, name, license_type, car):
        self.name = name
        self.license_type = license_type
        self.driving = False
        self.car = car
    
    def drive(self):
        if self.driving:
            print(f"{self.name} is already driving.")
        else:
            self.driving = True
            print(f"{self.name} is now driving.")
        action = input()
        match action:
            case "accelerate":
                self.car.accelerate()
                print(self.car.speed)
            case "brake":
                self.car.brake()
            case "stop":
                self.car.stop()
            case _:
                print("That's not an option.")

    def start_car(self):
        if self.car.on:
            print(f"{self.car.brand} is already on.")
        else:
            self.car.start()
            print(f"{self.car.brand} is now on.")

class Car:
    def __init__(self, brand):
        self.brand = brand
        self.on = False
        self.speed = 0
    
    def start(self):
        self.on = True
    
    def turn_off(self):
        self.on = False
    
    def accelerate(self):
        self.speed += 5
    
    def stop(self):
        while self.speed > 0:
            self.speed -= 5
    
    def brake(self):
        self.speed -= 5
    

person1 = Person("Geo", "B2", Car("Toyota"))

option = input("Do you want to start driving or start the car? ")
person1.start_car()
match option:
    case "drive":
        if not person1.car.on:
            print("You must turn the car on first")
        else:
            person1.drive()
