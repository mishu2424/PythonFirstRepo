# 1st Exercise
# Write a Program to input 2 numbers & print their sum.

""" first_Value=int(input("Enter the first integer value: "))
second_Value=int(input("Enter the second integer value: "))

print("The sum is:", first_Value+second_Value) """

# 2nd Exercise
#Write a program to input side of a square & print its area.
""" 
side=int(input("Enter the side of the square(integer value): "))

print("The area of the square is :",side*side) """

#3rd Exercise
#WAP to input 2 floating point numbers & print their average

""" num1=float(input("Enter the first number(float): "))
num2=float(input("Enter the second number(float): "))

print("The average is :", (num1+num2)/2) """

#4th Exercise
#WAP to input 2 int numbers, a and b. Print True if a is greater than or equal to b.If not print False.

""" a=int(input("Enter the first number(integer): "))
b=int(input("Enter the second number(integer): "))

print(a>=b) """

#LearnPyhton.org Exercise-
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring) 
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

#Here even if we don't use the format specifiers %s,%f,%d, It won't be an issue in Python. But we can use it to have the result according to our specific format.
#isinstance checks if the variable is in the format we want. 