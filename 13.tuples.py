my_tuples=(1, 2, 3, 4, 5)
#In case of single value in a tuple a comma(,) is must
#my_tuples=(1, )
print(type(my_tuples))
print(my_tuples)
my_tuples2=(1, 3, "Hello", 6.75) #JUST LIKE LISTS.
print(my_tuples2)
###DIFFERENCE BETWEEN LISTS AND TUPLES-
#LISTS ARE MUTABLE MEANING WE CAN CHANGE OR MODIFY THE VALUE OF LISTS, ON CONTRARY, TUPLES ARE IMMUTABLE MEANING NON-CHANGABLE.

#LIKE STRING & LISTS WE CAN ACCESS THE TUPLES THROUGH INDEXING-
print(my_tuples[2])
print(my_tuples2[-1])

#JUST STRING & LISTS WE CAN ALSO DO INDEX SLICING HERE-
print(my_tuples2[:len(my_tuples2)])
print(my_tuples2[::-1])

#NESTED TUPLES-
my_tuples3=([2,5,4,7],(3,6,8))
print(my_tuples3[1])
print(my_tuples3[1][0])

#TWO BUILT_IN TUPLE METHODS-
my_tuples4=(1,2,3,3,4,5,6,7,7)
print(my_tuples4.count(3))
print(my_tuples4.index(3)) #It gives the first index occurence of where 2 is stored.

#TUPLE ASSIGNMENT-
""" a=1
b=2
# or
a,b=1,2 """
#NOW TUPLE ASSIGNMENT IS COMMONLY USED IN SWAPPING-
a,b=1,2
a,b=b,a
print(a,b)

##SORTING A TUPLE WITH THE HELP OF LIST-
a_tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
a_list=list(a_tuple)
a_list.sort(reverse=True)
print(tuple(a_list))