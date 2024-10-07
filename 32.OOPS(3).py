##Inheritance
##When one class(derived/child) derives the properties and methods of another class(parent/base).
##There are three types of inheritance-
#1.Single Inheritance
#2.Multi-level Inheritance
#3.Multiple Inheritance


##Single Inheritance -
""" class Car:
    color="Red"
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car Stopped")
    

class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name
    def __init__(self,type):
        self.type=type
        self.start()

car1=ToyotaCar("Fortunar")
car1.stop()
print(car1.color) """

##Super() method in single level inheritance
##Super() method is used to access the properties of parent class.
##Point to be noted- You can inherit the methods using inheritance but can't access especially __init__() constructor of the parent class.
""" class Car:
    def __init__(self,type):
        self.type=type
        print(self.type)
    color="Red"
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car Stopped")
    def numberPrint(self,n):
        print(n)

class ToyotaCar(Car):
    def __init__(self,brand,type):
        super().__init__(type) ##Accessing the attributes of parent class.
        super().start() ##Accessing the methods of parent class.
        self.brand=brand
    

car1=ToyotaCar("Fortunar","Electric")
print(car1.brand)
print(car1.type) """
##Multi-level inheritance
##When there is __init__() constructor has been defined in toyotaCar(Car) class, the immediate child class Fortunar(toyotaCar) 
# will NOT be able to directly access the constructor of class Car().

""" class Car:
    def __init__(self,brand):
        self.brand=brand
    @staticmethod
    def start():
        print("Car started")
    @staticmethod
    def stop():
        print("Car stopped")
class toyotaCar(Car):
    discount="20% OFF"
    def __init__(self,price,brand):
        super().__init__(brand)
        self.price=price
class Fortunar(toyotaCar):
    def __init__(self,type,price,brand):
        super().__init__(price,brand)
        self.type=type
car1=Fortunar('Electric',"CAD 40000","2024 edition")
print(car1.type)
print(car1.discount)
print(car1.price)
print(car1.brand)
car1.start()
car1.stop() """
##When there is no __init__() constructor has been defined in toyotaCar(Car) class, the immediate child class Fortunar(toyotaCar) 
# will be able to access the constructor of class Car().
""" class Car:
    def __init__(self,brand):
        self.brand=brand
    @staticmethod
    def start():
        print("Car started")
    @staticmethod
    def stop():
        print("Car stopped")
class toyotaCar(Car):
    discount="20% OFF"
class Fortunar(toyotaCar):
    def __init__(self,type,brand):
        super().__init__(brand)
        self.type=type
car1=Fortunar('Electric',"2024 edition")
print(car1.type)
print(car1.discount) 
print(car1.brand)
car1.start()
car1.stop() """
##Multi-level Inheritance using super() method
""" class Car:
    def __init__(self,brand,type):
        self.brand=brand
        self.type=type
    @staticmethod
    def start():
        print("Car started")
    @staticmethod
    def stop():
        print("Car stopped")
class Hyundai(Car):
    def __init__(self,name,color,brand,type):
        super().__init__(brand,type)
        self.name=name
        self.color=color
    def colorOfCar(self):
        print(self.color)
class Elantra(Hyundai):
    def __init__(self,name,color,brand,type,price):
        super().__init__(name,color,brand,type)
        self.price=price
    
car1=Elantra("Hyundai Elantra","Red","2024 edition","Electric","CAD 37000")
print(car1.name)
print(car1.color)
# print("Price:"+car1.price)
print(f"Price: {car1.price}")
car1.start()
car1.stop() """

##Multiple inheritance
""" class Car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("Car started")
    @staticmethod
    def stop():
        print("Car stopped")
class Bike:
    def __init__(self,brand):
        self.brand=brand
    price="CAD 22000"
class Vehicle(Car,Bike):
    def __init__(self,year):
        self.year=year

v1=Vehicle("2024")
print(v1.year)
print(v1.price)
v1.start()
v1.stop()
 """
##Multiple inheritance using super() and direct method Invocation.
class Car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("Car started")
    @staticmethod
    def stop():
        print("Car stopped")
class Bike:
    def __init__(self,name):
        self.name=name
    @staticmethod
    def start():
        print("Bike started")
    price="CAD 22000"
class Vehicle(Car,Bike):
    def __init__(self,year,type,name):
        super().__init__(type)
        Bike.__init__(self,name)
        ##OR WE CAN USE DIRECT METHOD INVOCATION
        # Car.__init__(self,type)
        # Bike.__init__(self,name)
        self.year=year

v1=Vehicle("2024","Disel","Suzuki")
print(v1.year)
print(v1.price)
print(v1.type)
print(v1.name)
v1.start()
v1.stop()



##MRO Multiple Inheritance from chatgpt
class A:
    def __init__(self):
        print("Initializing A")

class B(A):
    def __init__(self):
        super().__init__()  # Calls A's __init__
        print("Initializing B")

class C(A):
    def __init__(self):
        super().__init__()  # Calls A's __init__
        print("Initializing C")

class D(B, C):
    def __init__(self):
        super().__init__()  # Calls B's __init__, which calls C's __init__, which calls A's __init__
        print("Initializing D")

d = D()



