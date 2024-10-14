#Different ways to define string-
""" str1='Hello'
str2="Hello" """
# str3=""" Hello """

#We can write multiple lines in a string and also can use escape sequence characters(\n,\t).
# str4="This is a string.\nWe are writing it in Python."

#Basic operations of strings-

#Concatenation-

""" str5="Hello"
str6="World!"
str7=str5+" "+str6
print(str7) """

#length
# print(len(str7)) #Spaces also get counted.

#INDEXING
""" str8="Hello world!"
print(str8[4]) """

#We can't modify the characters only can access.
# str8[0]="@" #IT IS NOT ALLOWED IN PYTHON.

#SLICING strname[star:stop:step]
str9="hello World!"
str10="ByE WoRlD!"
print(str9[2:6])
print(str9[:4])#Same as str9[0:4]
print(str9[:len(str9)])
print(str9[2:])#same as str9[2:len(str9)]
print(str9[0:len(str9):2])
print(str9[2:len(str9):3])

#Negative indexing
print(str9[-8:-5])
#Reversing-
print(str9[: :-1])

#Other functions
print(str9.endswith("ld!")) #It returns true/false
print(str9.capitalize()) #It creates a new string with the first letter being capitalized. It doesn't make any changes to the original string.
print(str9)#The string remains same after capitalization.
print(str9.replace("hello","Bye"))
print(str9.find("o"))
print(str9.find("World!"))
#find function returns -1 if the substring doesn't exist in the string.
print(str9.find("tata")) 
print(str9.count("o"))
print(str10.swapcase()) #It converts uppercase to lowercase and lowercase to upper.
print(','.join(str9))
print(str9.split())
print(str9.upper())
print(str10.lower())
print(str9.casefold())

""" The casefold() method is similar to the lower() method but it is more aggressive. This means the casefold() method converts more characters into lower case compared to lower() .

For example, the German letter ß is already lowercase so, the lower() method doesn't make the conversion.

But the casefold() method will convert ß to its equivalent character ss.
Using casefold(): gross
Using lower(): groß """