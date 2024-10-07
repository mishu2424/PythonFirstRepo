##To map with real world scenarios, we started using objects in code, This is called object oriented programming.
##A class is a blueprint for creating objects. It is a collection of data and methods. In Python, we write class name in Upper Camel Case (also known as Pascal Case), in which each word starts with an uppercase letter. For example: StudentInformation
##Objects are instances of class.
##Constructor- A constructor is a function(__init__) inside the class, which is invoked or called automatically whenever an object has been initiated/created. 
##A constructor always takes a parameter called 'self'(it doesn't always have to be 'self', it can be of other names but in the world of programming, 'self' is preffered more), which is a reference for the objects.
##Two types of constructors are 1.default and 2.parameterized.
##Attributes are variables of classes and objects.
##Two types of attributes 1.class attribute 2.object attribute
##Class attributes are created outside the constructor. It is usually created, when a data is common for every object.
##Object attributes are created inside the constructor, when a data is not same for every object created.
##But if there are attributes under same name in both class and constructor, in that case the precedence is higher for object attributes.
##Meaning obj.attr>class.attr 
##Methods are functions that belong to objects.Methods represent the functionality of the instances of the class.
##Static Method - Static method is a method that don't use the self parameter.(work at class level)
##It is created inside the class using the decorator @staticmethod which takes a function as parameter and returns a function without permanently modifying it.
##An example-
""" class <ClassName>:

    <class_attribute_name> = <value> ##Class attribute

    def __init__(self,<param1>, <param2>, ...):
        self.<attr1> = <param1> ##Object attribute (object attribute>class attribute)
        self.<attr2> = <param2> ##Object attribute (object attribute>class attribute)
        .
        .
        .
        # As many attributes as needed

    def <method_name>(self, <param1>, ...):  ##Method
       <code> 
       
    @staticmethod
    def hello():
        print("Hello")
      

   # As many methods as needed 

   """
""" Default Arguments
We can also assign default values for the attributes and give the option to the user if they would like to customize the value.

In this case, we would write <attribute>=<value> in the list of parameters.

This is an example:

class Circle:

    def __init__(self, radius=1):
        self.radius = radius 
        
# Default value
>>> my_circle1 = Circle()

# Customized value
>>> my_circle2 = Circle(5) 
        """
##Updating an instance attribute
""" >>> class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age


>>> my_dog = Dog("Nora", 10)

>>> my_dog.name
'Nora'

# Update the attribute
>>> my_dog.name = "Norita"

>>> my_dog.name
'Norita' """

##There are FOUR PILLARS of OOPS-
#1.Abstraction- Hiding the implementation details of a class and only showing the essential features to the user. 
#2.Encapsulation- Wrapping data and functions into a single unit(object).
#3.Inheritance
#4.Polymorphism