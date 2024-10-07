#Loops are used to repeat instructions.
#Two types of loops in Python- while loop and for loop
##break & Continue keywords

##break keyword is used to terminate a loop when encountered, It helps us to get out of a loop in the middle of iteration once our work is done.
##An example-
print("Break:")
i=1
while(i<=5):
    if(i==3):
        break ##Loop will be terminated, thus output will be just 1,2
    print(i)
    i+=1
    
##Continue keyword terminates execution in the current iteration & continue execution of the loop with the next iteration,
#It helps to skip something.
print("Continue:")
j=1
while(j<=5):
    if(j==3):
        j+=1
        continue #It will skip 3
    print(j)
    j+=1
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
print(a_set) """
# Infinite While Loops
# When we write and work with while loops, we can have something called an "infinite loop."
# If the condition is never False, the loop will never stop without external intervention.
# This usually happens when the variables in the condition are not updated properly during the execution of the loop.



##FOR LOOP
##FOR LOOPS ARE USED FOR SEQUENTIAL TRAVERSAL. FOR TRAVERSING A LIST, STRING, TUPLES ETC.
##FOR EXAMPLE LIST
nums=[2,4,3,65,7,"hello",3.45]
for item in nums:
    print(item)

##FOR TUPLES(WITH ELSE)
##Unlike languages like C,CPP.. we can use else for loops.
#  When the loop condition of "for" or "while" statement fails then code part in "else" is executed.
#  If a break statement is executed inside the for loop then the "else" part is skipped.
#  Note that the "else" part is executed even if there is a continue statement.
tup=(4,56,"Hello",(34,5),[34])
for tup_items in tup:
    print(tup_items)
else:
    print("END")   

##FOR STRING
str="STRING"
for l in str:
    print(l)
else:
    print("END")

##RANGE() function
##RANGE FUNCTION RETURNS A sequence of numbers, starting from 0(by default), increments by 1(by default), and stops before a specified number.
##range(?start,stop,?step)
## 3 ways to write range function
for i in range(5):
    print(i)

for j in range(1,5):
    print(j)

for k in range(1,5,2):
    print(k)


##FOR EVEN NUMBERS FROM 0 to 100
for even in range(0,100,2):
    print(even)

##PASS STATEMENT
##pass is a null statement that does nothing. It is used as a placeholder for future code.

for el in range(10):
    pass
if(i>5):
    pass