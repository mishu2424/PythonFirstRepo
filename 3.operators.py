a=5
b=2

# Arithmetic operations
print(a+b)
print(a-b)
print(a*b)
print(a/b) #divison operator always gives output in float type form
print(a%b)
print(a**b) #It mean a^b
lotsofhellos = "hello" * 10
print(lotsofhellos)
#Using operators with lists
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)
#Just like strings-
print([1,2,3] * 3)

#Relational operations
print(a==b) #Output will be in boolean form
print(a!=b) #Output will be in boolean form
print(a>=b) #Output will be in boolean form
print(a<=b) #Output will be in boolean form

#Assignment operations
a+=10 #(a=a+10)
#other assignments -=,*=,/=,%=,**=
print(a)

#Logical operations
c=50
d=30

print(not False)
print(not (c>d))
print((c==d) and (c>d))
print((c==d) or (c>d))