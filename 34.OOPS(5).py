#Polymorphism: Operator Overloading
#-->When the same operator is allowed to have different meaning according to the context.
#Some dundar operators and functions-
""" 
__add__ (addition)
__sub__ (subtraction)
__mul__ (multiplication)
__truediv__ (division)
__mod__ (modulus)

"""
#creating a class Complex realpart+imgainary part
#Goal is to create a class where it takes two complex numbers for example 1i+4j and 4i+1j, returns 5i+5j
""" class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def showNumber(self):
        return f"{self.real}i+{self.img}j"
    def sum(self,complex2):
        newReal=self.real+complex2.real
        newImg=self.img+complex2.img
        return Complex(newReal,newImg)
        
    

complex=Complex(1,4)
complex2=Complex(4,1)
print(complex.showNumber())
print(complex2.showNumber())
complex3=complex.sum(complex2)
print(complex3.showNumber()) """
##Here firstly, we created an instance of class Complex which is complex where the real part is 1, imginary part is 4.
##Secondly, we created a second instance of class Complex where the real part is 4, imaginary part is 1.
##Thirdly when we used complex3 to get an object of class Complex as the sum() method returns a new complex object, 
# hence why now complex3 is also an instance of class Complex even though it was not explicitly declared before the line.
##When we wrote complex.sum(complex2), the values for the real part and imaginary part was already defined previously for complex and complex2.
##So what it does, the sum() method considered complex as self argument and thus added its' real part with complex2's real part and same for imginary parts.
##Here is how complex3 has been become an instance of class Complex-
# return Complex(newReal, newImg)
# This line creates a new Complex object using the calculated newReal and newImg.
# The Complex constructor (__init__) is called here, which initializes a new complex number with the summed values.
# When you execute complex3 = complex.sum(complex2), it does the following:
# Calls the sum method on the complex instance, passing complex2 as the argument.
# Inside the sum method, a new Complex object is created (let’s say it represents 5 + 5j if both input numbers were 1 + 4j and 4 + 1j).
# This new object is returned from the method and assigned to complex3.


##Ok, now heading back to the goal, in this code above we used our logics to find the solution for complex numbers.
##But suppose we just want the user to write complex+complex2 instead of calling sum() method directly.
##In that case, we have to use dundar functions(__add__). For example, redifining the code all over again-
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def showNumber(self):
        return f"{self.real}i+{self.img}j"
    def __add__(self,complex2): #here __add__ is a dundar method which takes only one more argument beside self.
        if not isinstance(complex2, Complex):
           return NotImplemented

        newReal=self.real+complex2.real
        newImg=self.img+complex2.img
        return Complex(newReal,newImg)
        
    

complex=Complex(1,4)
complex2=Complex(4,1)
print(complex.showNumber())
print(complex2.showNumber())
complex3=complex+complex2
print(complex3.showNumber())