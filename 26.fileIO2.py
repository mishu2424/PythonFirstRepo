##Combining the mode.(r+,w+,a+)
##r+ mode(reading and writing)
##Cursos starts from the beginning
##It doesn't truncate(overwrite) the whole existed data from the file but overwrite it word by word from the starting even though it's in writing mode.
##Interesting fact is that even though it's also in writing mode,
#  it won't create a new file which doesn't already exist in the file which was possible using only the writing mode.
##For example when I tried to open this file, I didn't create it beforehand,so showed me an error.
""" f=open("sample2.txt","r+")
data=f.read()
f.close() """

""" f=open("demo2.txt","r+")
data=f.write("Hey,Hi")
print(f.read()) #It will print an empty space as the cursor in twxt file is already at the end of the last character.
f.close() """

##Truncating(Overwriting)
""" f=open("demo2.txt","r+")
data2=f.write("Bye")
print(f.read()) ##Now It will print just ',Hi' as the cursor was alread after the first three characters.
f.close() """

##w+ mode(writing and reading)
##This mode will create a new file if it already doesn't exist.
##It will truncate/overwrite the whole data.
""" f=open("demo3.txt","w+") 
# print(f.read()) #It will overwrite all the data as the cursor is at the beginning of the file .
f.write("Hey, Hello")
print(f.read()) ##It will print nothing as the cursor is alread at the end of last character.
f.close() """

##a+ (writing and reading)
##Creates a file if doesn't exist in the file.
##Cursor is at the end of the file.
##Doesn't truncate datas from the file.
f=open("demo4.txt","a+")
f.write("Hey, How is it going?")
print(f.read()) #Prints empty space as the cursor is at the end.
f.close()

##Diference between r+,w+,a+
##r+ it doesn't truncate the whole data.
##w+ it truncates the whole data
##a+ it doesn't truncate.