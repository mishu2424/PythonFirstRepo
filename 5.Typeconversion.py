#There are two types of type conversion (type conversion and type casting)
#type casting is automatically get done by compilers during run time.
#type casting is when we try to do something forcefully.
#The code below is an example of type conversion
a=2
b=4.25
print(a+b)
#here a is an integer value and b is a float so what will happen is that compiler will automatically convert the integer value of a into float value (2.0) as it considers float is superior over integer. 
# Thus the result will be in float form. It is called type conversion.

#Now, on the other hand, in case of type casting

""" c="2"
d=4.25
print(c+d) """

#The code above will give an error as in python we can not add a string with a float or integer value which we can do between an integer and a float, thanks to type conversion.
#But if we want to forcefully do it, we can do so by type casting.
c=int("2")
d=4.25
print(type(c))
print(c+d)
#This is called type casting.