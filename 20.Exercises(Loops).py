#Practice questions-
##Print numbers from 1 to 100.
""" i=1
while(i<=100):
    print(i)
    i+=1 """
##Print numbers from 100 to 1
""" i=100
while(i>=1):
    print(i)
    i-=1 """

##Print the multiplication table of a number.
""" n=int(input("Enter a number: "))
print("Multiplication of",n)
i=1
while(i<=10):
    print(n*i)
    i+=1 """

##Print the elements of the list using a loop. [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
""" a_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
j,maxvalue,sum=0,0,0

while(j<len(a_list)):
    ##TRAVERSING THE LIST
    print(a_list[j]) 
    ##SUM 
    sum+=a_list[j]    
    j+=1
print("Sum of elements in the list:", sum) """

"""   ##FINDING THE MAXIMUM NUMBER
    if(maxvalue<a_list[j]):
        maxvalue=a_list[j]  """
    
# print("Maximum value:", maxvalue)
##Search for a number x in this tuple using loop. (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
""" a_tuple = (1, 4, 9, 16, 25, 36, 36, 49, 64, 81, 100)
n=int(input("Enter the number: "))
i,found=0,0
while(i<len(a_tuple)):
    if(a_tuple[i]==n):
        print("Number exists in the list and it was found in index", i)
        found=1
    i+=1
if(not found):
        print(n, "doesn't exist in the list")  """


##Finding all the odd numbers from 1 to 30
""" a_set=set()
k=0
while(k<=30):
    if(k%2==0):
        k+=1
        continue
    else:
        print("Odd Number: ",k)
        ##OR WE CAN STORE THEM IN A SET/list
        a_set.add(k)
    k+=1        
print(a_set)  """       

##WAP TO FIND THE SUM OF FIRST N NUMBERS USING WHILE LOOP.
""" n=int(input("ENTER A NUMBER UNTIL WHICH YOU WANT THE TOTAL SUM: "))
i,sum=n,0
while(i>=1):
    sum+=i
    i-=1

print("Total: ",sum) """

##USING FOR LOOPS

##WAP TO PRINT THE ELEMENTS OF THE FOLLOWING LIST USING A LOOP
""" a_list=[1, 4, 9, 16, 25, 36, 49, 64, 81, 49, 100]
for item in a_list:
    print(item) """
##SEARCH FOR A NUMBER X IN THIS TUPLE USING A LOOP (THIS PROCESS IS CALLED LINEAR SEARCH)
""" a_tuple=(1, 4, 9, 16, 25, 36, 49, 64, 81, 49, 100)
print(a_tuple)
index=0
n=int(input("ENTER A NUMBER FROM THIS LIST ABOVE:"))
for item_of_tuple in a_tuple:
    if(n==item_of_tuple):
        print("FOUND! At index",index)
    index+=1
else:
    print("END")     """

##WAP TO FIND THE FACTORIAL OF FIRST N NUMBERS.(USING for)
""" n=int(input("ENTER A NUMBER TO GET ITS' FACTORIAL: "))
fact=n
for i in range(n-1,1,-1):
    fact=fact*i
    print("factorial of", n, "*", i, "=", fact) """
##RANGE
##Print numbers from 100 to 1 USING for loop and range
""" for number in range(100,1,-1):
    print(number) """

##Print the multiplication table of a number USING FOR LOOP AND RANGE 
""" n=int(input("Enter a number: ")) 
print("Multiplication of this number:")
for i in range(1,11):
    print(n*i) """

#Write a program which repeatedly reads number from user until user enters done.Once done is entered, print out the total, count and average
#of the numbers. If users enters anything than a number, detect their mistake using try and except and skip to the next number.
""" done=False
total=0
count=0
while not done:
    number=input("Enter a number: ")
    try:
        if(number is 'done'):
            done=True
        number=float(number)
    except:
        print("Error input! Enter a valid number")
        continue
    total+=number
    count+=1
print(f"Total= {total}")
print(f"Counts= {count}")
print(f"Average= {total/count}") """
#Write a program which repeatedly reads number from user until user enters done.
# Once done is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.
done=False
total=0
count=0
largest_numb=-1
smallest_num=None
while not done:
    number=input("Enter a number: ")
    try:
        if(number == 'done'):
            done=True
            continue
        number=int(number)
    except:
        print("Invalid input")
        continue
    if(largest_numb<number):
        largest_numb=number
    if(smallest_num is None):
        smallest_num=number
    if(smallest_num>number):
        smallest_num=number
print(f"Maximum is {largest_numb}")
print(f"Minimum is {smallest_num}")
