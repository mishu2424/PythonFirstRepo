#Dictionaries are used to store data values in key:value pairs.
#There are unordered(meaning no index),mutable & don't allow duplicate keys.
#The keys of a dictionary must be of an immutable data type.
#For example, they can be strings, numbers, or tuples but not lists since lists are mutable.
#The values of a dictionary can be of any data type,
#so we can assign strings, numbers, lists, tuple, sets, and even other dictionaries as the values
info={
    #"Key":"Value"
    "name":"Mishu",
    "subjects":["C","Python","Java"],
    "topics": ("dict","set"),
    "is_adult":True,
    12.99:94.44,
    45:45,
    ("Hi","hello"):["tata","Bye"]
    #Meaning key can be of any data type except lists & dictionaries and set as they are mutable.. 
}

print(type(info))
print(info)
print(info["name"])
print(info[12.99])
print(info[("Hi","hello")])
#Dictionaries are mutable so it can be changed any time -
info["name"]="Apurbo Dey Mishu"
print(info)
#We can also add a key in the dictionary if we want to.
info["Age"]=24
print(info)
#We can also delete it if we want to-
del info["Age"]
print(info)
#A dictionary can be null-
null_info={}
print(null_info)
#We can also create keys for the null dictionary-
null_info["name"]="Apurbo Dey Mishu"
print(null_info)


#Nesting dictionary-
marks_info={
    "name":"Mishu",
    "marks":{
        "Phy":84,
        "Chem":88,
        "Math":95
    }
}
#We can access it like this-
print(marks_info["marks"])
print(marks_info["marks"]["Chem"])

##DICTIONARY METHODS-
info2={
    #"Key":"Value"
    "name":"Mishu",
    "subjects":["C","Python","Java"],
    "topics": ("dict","set"),
    "is_adult":True,
}

#keys method
print(info2.keys())
print(type(info2.keys()))
#It's a dictionary type. To conver it to a list we can do type casting-
# print(list(info2.keys()))

#len method-
print(len(info2))
#OR
print(len(info2.keys())) 

#Values method-
print(info2.values())
# print(list(info2.values()))

#Items method(return all the (key:value) pairs as tuple)
# print(marks_info.items())
print(info2.items())

#Get method-
print(info2.get("name")) #It returns the value of the keys.

#Now the question is what is the difference between get method and normal way of getting a value of a key like this-> info2["name"] ??
#In general way, when we want to access a key in a dictionary which doesn't exist in the dictionary, will return error after the runtime.
#But get() method will return none if the key doesn't exist in the dicttionary.

#For instance-
# print(info2["name2"])  #this will return error as this key doesn't exist in the dictionary above and the remainder of the code will not run But 

print(info2.get("name2")) #this will return none not an error meaning the remanider of the code will execute regardless of the output of this method.
#OR
#We can also replace none return with a message we want to show-
print(info2.get("name2","Not found"))

##Update Method-
info2.update({"age":24})
print(info2)
#We can also insert a new dictionary-
marks={
    "Phy":80,
    "Chem":87,
    "Math":98
}
info2.update(marks)
print(info2)

#Pop Method-
info2.pop("age")
print(info2)

#Popitem Method(Remove the last item)-
info2.popitem()
print(info2)

#Clear Method-
info2.clear()
print(info2)