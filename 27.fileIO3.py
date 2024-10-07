##with syntax
##When using with syntax, we don't necessarily need to close the file.With syntax automatically closes the file.
""" with open("demo5.txt","w") as f:
    f.write("Hi, buddy!")

with open("demo5.txt","r") as f:
    print(f.read()) """

##Deleting a file using OS module.
##Module is a code library/file written by another programmer that generally has a function we can use.
import os
if os.path.exists("demo6.txt"):
    os.remove("demo6.txt")
else:
    print("File doesn't exist!")
