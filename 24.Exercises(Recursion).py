##FACTORIAL
def fact(n):
    if(n==1 or n==0):
        return 1
    return n*fact(n-1)
print(fact(3))

##FIBONACCHI
##0,1,1,2,3,5,8,13
def fibo(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    return fibo(n-1)+fibo(n-2) 
print(fibo(4))

##Write a recursive function to calculate the sum of first n natural numbers.

def sumOfNatural(n):
    if(n==1):
        return 1
    return sumOfNatural(n-1)+n

print(sumOfNatural(5))

##Write a recursive function to print all the elements in alist.
a_list=[1,4,5,7]
print("Traverse through the list using recursion: ")
def traverse(n):
    if(n==len(a_list)):
        return
    print(a_list[n],end=" ")
    traverse(n+1)

traverse(0)
print()
print("Reverse traverse through the list using recursion: ")
def reverseTraverse(n):
    if(n<0):
        return
    print(a_list[n] ,end=" ")
    reverseTraverse(n-1)
   
    
reverseTraverse(len(a_list)-1)