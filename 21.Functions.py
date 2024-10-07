##Function is a block of statements that performs a specific task.
##We use function to reduce redundancy and enhance the reusuability.

##FOR example 
##To calculate a sum of two numbers-
def calc_sum(a,b):##THIS PROCESS IS CALLED FUNCTION DEFINITION. THE VALUES WE PASSED THROUGH IT ARE CALLED PARAMETERS.
    # print(a+b) ##I can do both return or print inside this.
    return a+b

sum=calc_sum(23,33)##THIS PROCESS IS CALLED FUNCTION CALL. THE VALUES WE PASSED THROUGH IT ARE CALLED ARGUMENTS.
print(sum)

sum2=calc_sum(23,55) ##THIS PROCESS IS CALLED FUNCTION CALL. THE VALUES WE PASSED THROUGH IT ARE CALLED ARGUMENTS.
print(sum2)
##Built-in functions
print("Hello","World")
##with sep=""
print("Hello","world",sep="")
##with end=" "
print("Hello",end=" ")
print("World")
##Default Parameters
##Assigning a default value to parameter, which is used when no argument is passed.

def multi(a=1,b=2):
    print(a*b)
multi() 

##It is also possible
def multi(a,b=2):
    print(a*b)
multi(1) 
#It is NOT possible-
""" def multi(a=1,b):
    print(a*b)
multi()  """