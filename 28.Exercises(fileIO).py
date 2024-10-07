##Create a new file "practice.txt" using python. Add the following data in it:
#Hi everyone.
#we are learning File I/O
#Using Java
#I like Programming in Java.
""" with open("practice.txt","a") as f:
    f.write("Hi everyone.\nWe are learning File I/O.\nUsing Java.\nI like Programming in Java.") """

##WAF that replaces all occurrences of "java" with "python" in above file.
""" with open("practice.txt","r") as f:
    data=f.read()
    print(data)
    print(type(data)) 
new_data=data.replace("Java", "Python")
with open("practice.txt","w") as f:
    f.write(new_data) """

##Search if the word learning exists in the file or not.
""" with open("practice.txt","r") as f:
    data=f.read()
    #value in container, it actually turns that into a call to the appropriate dunder method __contains__,
    #  which means that Python actually runs the expression container.__contains__(value).
    if("learning" in data):
        print("Learning word exists!")
    else:
        print("Not found!") """

##WAF to find in which line of the file does the word "learning" occur first. Print -1 if word not found.
""" line=0
with open("practice.txt","r") as f:
    data=f.readline()
    if(data.find("learning")!=-1):
        print("Found in Line 1")
        line=1
    data=f.readline()
    if(data.find("learning")!=-1):
        print("Found in Line 2")
        line=2
    data=f.readline()
    if(data.find("learning")!=-1):
        print("Found in Line 3")
        line=3
    data=f.readline()
    if(data.find("learning")!=-1):
        print("Found in Line 4")
        line=4
    if(not line):
        print(data.find("learning")) """
##Another way to do this same code 
""" def check_line_no():
    line_no=1
    data=True
    with open("practice.txt",'r') as f:
        while data: ##will keep reading line until it is " " which is False
            data=f.readline()
            if("learning" in data):
                print("Found at line",line_no)
                return ##return from here if found.
            line_no+=1 #Updating the line number if not found in the current line.

    return -1   ##return -1 if not found

print(check_line_no()) """

##From a file containing numbers, separated by comma, print the count of even numbers.
""" def count_even_numbers():
    count=0
    with open("practice2.txt", 'r') as f:
        data=f.read()
        splitted=data.split(',')
        for i in range(len(splitted)):
            if(int(splitted[i])%2==0):
                print(splitted[i])
                print(type(splitted[i])) #the type still remains string.
                count+=1
        print("Total even number:",count)
        if(not count):
            print("No even number")   
count_even_numbers() """
##wITHOUT SPLIT() FUNCTION
def count_even_numbers():
    count=0
    num=""
    with open("practice2.txt", 'r') as f:
        data=f.read()
        print(data)   
        for i in range(len(data)):
            if(data[i]==","):
                print(num,end=" ")
                if(int(num)%2==0):
                    count+=1
                num=""
            else:
                num+=data[i]
           
        if(int(num)%2==0):
                count+=1
        print("Total even number", count)


count_even_numbers()