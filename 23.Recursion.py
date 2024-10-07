##A function that calls itself repeatedly.
def show(n):
    if(n==0):  #BASE CASE
        return
    print(n)
    show(n-1)

show(5)

##WHEN A RECURSION HAPPENS WITH NO BASE CASE, IT IS CALLED STACK OVERFLOW.
##A CONCEPT NAMED CALL STACK THAT EXISTS IN RECURSION BY THE LAYERS FUNCTION.
## AN EXAMPLE-
def show(n):
    if(n==0):  #BASE CASE
        return
    print(n)
    show(n-1)
    if(n==1):
        print("coming back from 1")
    if(n==2):
        print("coming back from 2")
    if(n==3):
        print("coming back from 3")
show(5)