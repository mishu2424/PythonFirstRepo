##Remove an Instance Attribute
""" >>> class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age


>>> my_dog = Dog("Nora", 10)

>>> my_dog.name
'Nora'

# Delete this attribute
>>> del my_dog.name

>>> my_dog.name
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    my_dog.name
AttributeError: 'Dog' object has no attribute 'name' """

##Delete an Instance
""" >>> class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age


>>> my_dog = Dog("Nora", 10)

>>> my_dog.name
'Nora'

# Delete the instance
>>> del my_dog

>>> my_dog
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    my_dog
NameError: name 'my_dog' is not defined """

##Private(like) attributes & methods
#Private attributes & methods are meant to be used only within the class and are not accessible from outside the class.
#Public and Private
class bankAccount:
    def __init__(self,acc_no,acc_pass):
        self.accountNumber=acc_no ##Public attribute
        self.__acc_pass=acc_pass ##Private attributes are created with double underscore(__).
        
    def resetPass(self):
        print(self.__acc_pass)

    ##Private method
    def __hello(self):  
        print("Hello person")

    def welcome(self):
        self.__hello()
        

##Now if I want to access the private attribute it will show me an error.
acc1=bankAccount("56747","654")
# print(acc1.__acc_pass)
print(acc1.resetPass())
print(acc1.__hello()) ##We can't access private methods from outside of the class.
##But if we call welcome() function, that will call the hello function as private methods are only accessible within the class, meaning other class methods can access the private methods.
print(acc1.welcome())