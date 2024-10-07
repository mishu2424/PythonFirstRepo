##Sets in Python-

#It is a collection of unordered(no-index) unique,immutable elements(Hashvalue). Meaning we can store any kind of data type except list and dictionary as they are mutable.
#Difference between dictionary and set is that elements in Dictionaries are mutable whereas elements in sets are immutable.
#SET ITSELF IS MUTABLE BUT THE ELEMENTS IN IT ARE IMMUTABLE(Hashvalue). 

#An example of how sets look like-
collection={1,2,3,4,(34,55)}
print(collection)
print(type(collection))

#Duplicate values are not allowed in sets and get ignored while dealing with-
collection2={1,3,3,3,2,4,4}
print(collection2) #Output will be {1,3,2,4}
print(len(collection2)) #length will be 4. 

#Now when we want to write a null set there is a different syntax for that-
null_set=set()
print(null_set)
print(type(null_set))

#Methods of Sets-
#ADD METHOD
null_set.add(1)
print(null_set)
null_set.add("Hi")
my_tuple=(23,"Hello",2.34)
null_set.add(my_tuple)
print(null_set)
#REMOVE METHOD
null_set.remove("Hi")
print(null_set)
#POP METHOD
null_set.pop()
print(null_set)
#Union METHOD
set1={1,2,3}
set2={3,4,5}
print(set1.union(set2)) #Combines values of each set and returns a new set.
##OR diiferent way to do it-
print(set1 | set2)
##IT can take multiple sets as arguments-
set3={5,6,7}
set4={7,8,9}
print(set1.union(set2,set3,set4))
##OR different way to do it-
print(set1 | set2 | set3 | set4)
#INTERSECTION METHOD
print(set1.intersection(set2)) #Returns a new set with common values between two sets.
##OR different way to do it-
common_set=set1 & set2
print(common_set)
#COPY METHOD
new_set=set1.copy()
print(new_set)
##UPDATE METHOD  
set1.update(set2) #COPIES ELEMENTS OF SET2 into SET1 IGNORING DUPLICATES LIKE UNION METHOD.
print(set1)
#CLEAR METHOD
null_set.clear()
print(null_set)

##DIFFERENCE METHOD
set5 = {"apple", "banana", "cherry"}
set6 = {"google", "microsoft", "apple"}
set7=set5.difference(set6)
print(set7)
