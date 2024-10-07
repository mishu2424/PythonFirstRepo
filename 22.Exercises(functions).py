##WAP TO FIND THE AVERAGE OF THREE NUMBERS.
""" sum=0
for i in range(3):
    n=int(input("Enter the value: "))
    sum+=n

print("Average:",sum/3)
 """
def average(a,b,c):
     print("Average: {:.2f}".format((a + b + c) / 3))
     print(f"Average is {(a+b+c)/3:.2f}.")
average(3,3,3)

##THIS PART IS JUST FOR FUN
""" for i in range(3):
     if(i==0):
          n1=int(input("Enter the first value: "))
          
     if(i==1):
          n2=int(input("Enter the second value: "))
          
     if(i==2):
          n3=int(input("Enter the third value: "))
          
     
average(n1, n2, n3) """

##Write a Function TO PRINT THE LENGTH OF A LIST WHERE LIST IS PASSED AS A PARAMETER .
""" a_list=[12,3.35,[34,"Hello"],(9,9.0),{34,"World"}]
def length(a_list):
     print(len(a_list))
     
length(a_list) """
##WAF TO PRINT THE ELEMENTS OF A LIST IN A SINGLE LINE.(LIST PASSED AS A PARAMETER)
""" a_list=[12,3.35,[34,"Hello"],(9,9.0),{34,"World"}]
def traverse(a_list):
    for item in a_list:
        print(item,end="")

traverse(a_list) """
##WAF TO FIND THE FACTORIAL OF N.
""" def factorial(n):
    fact=n
    for i in range(n-1,0,-1):
        fact=fact*i
    return fact
print(factorial(5)) """
##WAF TO CONVERT CAD TO BDT.
""" def currencyConverter(cad):
    bdt=cad*87.97
    print("CAD$",cad,sep="",end=" ")
    print("= BDT",bdt,"TK")

currencyConverter(5) """

""" Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
    Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours.
    Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation.
    The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
    You should use input to read a string and float() to convert the string to a number. 
    Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly.
    Do not name your variable sum or use the sum() function. """

def computepay(h, r):
    if(h<=40):
        return h*r
    elif h>40:
        normal_rate=40*r
        extra_rate=(h-40)*(r*1.5)
        return extra_rate+normal_rate
    

hrs = input("Enter Hours:")
r = input("Enter rates:")
try:
    hrs=float(hrs)
    r=float(r)
except:
    print("Invalid input")
    quit()
p = computepay(hrs,r)
print("Pay", p)
