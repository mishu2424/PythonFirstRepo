""" age= 24

if(age>=18):      #It only will work when satisfies the condition.
    print("Can vote & drive") #Indentation should be of at least 4 spaces.
elif(age<=18):    #elif statement works only when if statement returns false.Otherwise It won't work if 'if statement' returns true.
    print("Can't vote!") """
    

#It always works regardless of any positive/negative/or any value.
""" if(True):        
    print("can vote") """

marks=float(input("Enter your marks: "))
print(marks)
if(100<marks):
    print("Not a valid mark")
elif(100>=marks>=90):
    print("Grade: A")
elif(90>marks and marks>=80):
    print("Grade: B")
elif(80>marks>=70):
    print("Grade: C")
elif(70>marks>=60):
    print("Grade: D")
else:
    print("Fail")
