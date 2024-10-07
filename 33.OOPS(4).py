##Suppose we want to manipulate the class attribute-
""" class Person:
    name = "Anonymous"
    def updatename(self,name):
        ##WE CAN CHANGE THE ATTRIBUTE OF CLASS (name) -
        # self.__class__.name=name
        ##OR
        Person.name=name

p1=Person("Barsha")
print(Person.name)
print(p1.name) """
##But suppose instead of doing this, we want to directly access the class attribute in class function, 
# in that case class() method comes into the picture.
##class() -A class method is bound to the class & receives the class as an implicit first argument.
""" class Person:
    name= "Anonymous"
    @classmethod  #this decorator classmethod() takes a function and returns an improved function. 
    def updatename(cls,name):
        cls.name=name

p1=Person()
p1.updatename("Barsha")
print(Person.name)
print(p1.name)
 """

##As of now, we have studied 3 types of methods in class-
#1.Instance methods(self)
#2.Staticmethod()-> When we are not using any attribute of class or object as argument, not using any properties of class and object.
#3.ClassMethod(cls)-> When we want to directly access the attribute or properties of class method.

#Here in the example below when we changed the value of phy_mark the percentage didn't get changed it still considered he previous marks(98).
# But the percentage should've changed respective to the updated number, right? 
##To solve this issue we use @propertymethod
class student_marks:
    def __init__(self,phy_mark,chem_mark,math_mark):
        self.phy_mark=phy_mark
        self.chem_mark=chem_mark
        self.math_mark=math_mark
        self.percentage=(self.phy_mark+self.chem_mark+self.math_mark)/3

s1=student_marks(98,97,99)
print(f"Your percentage is {s1.percentage}%")
s1.phy_mark=95
print(f"Your new percentage is {s1.percentage}%")

##@propertymethod
""" class student_marks:
    def __init__(self,phy_mark,chem_mark,math_mark):
        self.phy_mark=phy_mark
        self.chem_mark=chem_mark
        self.math_mark=math_mark

    @property
    def percentage(self):
        return (self.phy_mark+self.chem_mark+self.math_mark)/3
s1=student_marks(98,97,99)
print(f"Your percentage is {s1.percentage}")
s1.phy_mark=95
print(f"Your percentage is {s1.percentage}") """
##We can also do this without using property method-
""" class student_marks:
    def __init__(self,phy_mark,chem_mark,math_mark):
        self.phy_mark=phy_mark
        self.chem_mark=chem_mark
        self.math_mark=math_mark
    def percentage(self):
        return (self.phy_mark+self.chem_mark+self.math_mark)/3

s1=student_marks(98,97,99)
print(f"Your percentage is {s1.percentage()}")
s1.phy_mark=95
print(f"Your percentage is {s1.percentage()}") """
#Comparison between these two is that in normal method, we need to use parenthesis when calling the method while
# in property method, we don't need to use that.
""" 1. Cleaner Syntax:
With @property, you can access the method like an attribute, which makes the code more intuitive and readable.
 For example, s1.percentage feels more like accessing a property than calling a method, enhancing the clarity of the code.
2. Encapsulation:
Properties allow you to hide the implementation details. 
You can change how the percentage is calculated or add additional logic later without changing the interface.
 Users of your class can still access s1.percentage without needing to know if it’s a method or computed property.
3. Read-Only Attributes:
By using @property, you can create read-only attributes easily.
 This means you can expose a value without allowing it to be modified directly, ensuring better control over how the data is accessed.
4. Dynamic Calculations:
If the value needs to be recalculated based on other attributes, using a property ensures it's always 
up to date without needing to remember to call a method after changing values. """
##Now an important concept-
##Getter method AKA Property method-
# The @property decorator in Python serves as a getter method, allowing you to retrieve values from attributes in a clean and controlled way.
# What is a Getter Method?
# A getter method is a method that allows you to access the value of an object's attribute.
#  It provides a way to retrieve the value while potentially adding some logic or computation when accessing that value.

# Using @property as a Getter
# Syntax: The @property decorator allows you to define a method that can be accessed like an attribute. 
# This means you can get the value without needing to call the method explicitly.
# An Example of Getter Method Using @property -
""" class Circle:
    def __init__(self, radius):
        self._radius = radius  # Using a leading underscore to indicate it's a private attribute

    @property
    def area(self):
        return 3.14 * self._radius ** 2  # Calculated property

# Creating an instance of Circle
circle = Circle(5)

# Accessing the area using the getter method
print(f"The area of the circle is: {circle.area}")   """# No parentheses needed

##Now Setter method-
# When you use the @property decorator for a getter,
#  you can also define a setter for the same property using the @<property_name>.setter syntax.
#  This allows you to control how an attribute is updated, including adding validation or transformation logic.

# Using Setters with @property
# Defining a Setter: To define a setter for a property,
#  you use the @<property_name>.setter decorator. This allows you to set the value of the property using an intuitive syntax.

# Encapsulation: Setters provide a way to encapsulate the logic for updating an attribute,
#  ensuring that any necessary checks or calculations are performed when the attribute's value is changed.
""" class Circle:
    def __init__(self,radius):
        self._radius=radius #We used private attribute.
    #getter
    @property
    def radius(self):
        return self._radius #If we used public attributes here it would be a recursion as the name for method and attrbiutes would be same.
    #Setter 
    @radius.setter
    def updated_Value(self,value):
        if(value<0):
            raise ValueError("Radius cannot be negative.")
        self._radius=value

    def area_square(self):
        return 3.14*(self._radius)**2
    
circle=Circle(5)
#Calling getter method
print(circle.radius)
print(circle.area_square())
#Calling setter to update the value-
circle.updated_Value=10
#getter
print(circle.radius)
print(circle.area_square()) """
##It's always better and common to use private attributes when using setter and getter method.
# It's not mandatory, but private attributes are more preferrable.        
##deleter
""" class Circle:
    def __init__(self,radius):
        self._radius=radius #We used private attribute.
    #getter
    @property
    def radius(self):
        return self._radius #If we used public attributes here it would be a recursion as the name for method and attrbiutes would be same.
    #Setter 
    @radius.setter
    def updated_Value(self,value):
        if(value<0):
            raise ValueError("Radius cannot be negative.")
        self._radius=value
    @radius.deleter
    def delete(self):
        del self._radius
    def area_square(self):
        return 3.14*(self._radius)**2
    
circle=Circle(5)
#Calling getter method
print(circle.radius)
print(circle.area_square())
#Calling setter to update the value-
circle.updated_Value=10
#getter
print(circle.radius)
#But we are deleting it before calculating here.
del circle._radius
#Also using the concet exception handling.
try:
    print(circle.area_square())
except AttributeError as e:
    print(e)
finally:
    print("Done!") """

