##File I/O
##Python can be used to perform operations on files.
##Type of files-
##1.Text file-.txt, .docx, .log etc.
##2.Binary file-.mp4, .mov, .png, .jpeg etc.

##To read a file 
# f=open("demo.txt","r")
""" data=f.read()
print(data)
print(type(data)) """
##We can even pass parameters using read() function.
""" piece_of_data=f.read(5)
print(piece_of_data) """

##To read a single line 
""" data2=f.readline() ##It reads the data in a single line and always leave a '\n' at the end of reading the line.
print(data2)
data2=f.readline()  ##Now it will read the second line.
print(data2) """

##One thing to remember is that if we read the files using both read() and readline(), the readline() function will return only empty spaces.
##For example-
""" data=f.read()
print(data)
print(type(data))

data2=f.readline() ##It reads the data in a single line and always leave a '\n' at the end of reading the line.
print(data2)
data2=f.readline()  ##Now it will read the second line.
print(data2) """
##But if we want to do both operations then we will have to close the file first and re-open the file again. 
""" data=f.read()
print(data)
print(type(data))
f.close()
f=open("demo.txt") #Default mode is read.
data2=f.readline() ##It reads the data in a single line and always leave a '\n' at the end of reading the line.
print(data2)
data2=f.readline()  ##Now it will read the second line.
print(data2)
f.close() """

##Now if I want to open a file that doesn't exists will give me an error.
""" f=open("sample.txt")
data=f.read()
print(data)
f.close() """

##But if I do the same using write mode or append mode, a new file will be opened with the name with which we are trying to fetch the data.
""" f=open("sample.txt","w")
data=f.write("Hey, Hi.") """

##Write mode
##One important thing about accessing a file using write mode is It overwrites the already existed data in the file.
##For example we again want to write something in sample.txt file, it will overwrite the Hey,Hi from thr file by replacing with new data.
""" data2=f.write("My name is Mishu")
f.close() """

##Now if We want to add something in the file keeping the previous data, we can do so by using append mode.
f=open("sample.txt","a")
data=f.write("Hey, Hi.\n")
data2=f.write("My name is Mishu")
f.close()

