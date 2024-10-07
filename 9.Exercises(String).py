#WAP to input user's first name and print it's length.

""" first_name=input("Enter your first name: ")
print("The name of your length is: ",len(first_name)) """

#WAP to find the occurence of $ in a string.

""" str=input("Enter a string containing($): ")
print(str.count("$"))
print(str.find("$")) """

""" 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
Convert the extracted value to a floating point number and print it out. """
text = "X-DSPAM-Confidence:    0.8475"
fpos=text.find('0')
extracted_output=text[fpos:len(text)]
print(float(extracted_output))