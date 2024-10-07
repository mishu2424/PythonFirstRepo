""" name=input("Enter your name: ")
age=input("Enter your age: ")
print(type(name))
print("Your name is ",name)
print(type(age))
print("Your age is ",age) """

#When we ran this code, the data type for age was a str which should have been an integer.
#So what we can learn from this is that input() function always gives a string type value.
#So, here comes the role of type casting.
#We can do type casting to expect the result according our desired(float/int) form.
#So, how we can do that is written below-
name=input("Enter your name: ")
age=int(input("Enter your age: "))
cgpa=float(input("Enter you cgpa: "))
print(type(name))
print("Your name is ",name)
print(type(age))
print("Your age is ",age)
print(type(cgpa))
print("Your CGPA is ",cgpa)
#Now when we ran this code, the data type and the result for age was in integer form.
