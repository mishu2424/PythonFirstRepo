#WAP to check if a number entered by the user is odd or even.

""" number=int(input("Enter a number to check if it's odd or even: "))

if(number%2==0):
    print(number,"is an even number.")

elif(number%2!=0):
    print(number,"is not an odd number") """

#WAP to find the greatest of 3 numbers entered by the user.
""" first_number=int(input("Enter first number: "))
second_number=int(input("Enter second number: "))
third_number=int(input("Enter third number: "))
fourth_number=int(input("Enter fourth number: "))

if(first_number>second_number and first_number>third_number and first_number>fourth_number):
    print("The biggest number is ",first_number)

elif(second_number>first_number and second_number>third_number and second_number>fourth_number):
    print("The biggest number is ",second_number)

elif(third_number>first_number and third_number>second_number and third_number>fourth_number):
    print("The biggest number is: ",third_number)

else:
    print("The biggest number is ",fourth_number) """

#WAP to check if a number is a multiple of 7 or not.

""" number=int(input("Enter a number to check if it's multiple of 7: "))
if(number%7==0):
    print(number,"is a multiple number of 7")

else:
    print(number,"is not a multiple number of 7") """











""" 3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
 Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
   Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
     You should use input to read a string and float() to convert the string to a number.
 Do not worry about error checking the user input - assume the user types numbers properly. """

""" hours=input("Enter hours: ")
h=float(hours)
rate=input("Enter the rates: ")
r=float(rate)

if(h<=40):
    print(h*r)
elif(h>40):
    normal_rate=40*r
    new_rate=((h-40)*(r*1.5))
    print(normal_rate+new_rate) """

""" 3.3 Write a program to prompt for a score between 0.0 and 1.0.
If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85. """
""" score=float(input("Enter your score(0.0-1.0): "))
if 0<=score and score<=1:
    if(score>=0.9):
        print("Grade: A")
    elif(0.9>=score>=0.8):
        print("Grade: B")
    elif(0.8>=score>=0.7):
        print("Grade: C")
    elif(score>=0.6):
        print("Grade: D")
    else:
        print("Grade: F")
else:
    print("Error! Invalid score")
    exit() """

