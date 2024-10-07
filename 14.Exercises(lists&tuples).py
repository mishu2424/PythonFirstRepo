#WAP to as the user to enter three names of their favorite movies and store them in a list.
""" fav_movies=[]
first_movie=input("Enter the name of first movie: ")
second_movie=input("Enter the name of second movie: ")
third_movie=input("Enter the name of third movie: ") """
#USING APPEND
""" fav_movies.append(first_movie)
fav_movies.append(second_movie)
fav_movies.append(third_movie) """
#USING EXTEND
""" fav_movies.extend([first_movie,second_movie,third_movie])
print(fav_movies)
 """
#Another way to do it-
""" fav_movies=[]
i=0
while(i<3):
    print("Movie no ",i+1)
    fav_movies.append(input("Enter movie's name: "))
    i=i+1

print(fav_movies) """

#WAP to check if a list contains a palindrome of elements.
""" a_list=[1,2,3,2,1]
b_list=a_list.copy()
a_list.reverse()
if(b_list==a_list):
    print("Palindrome")
else:
    print("Not Palindrome")

#Another one-
c_list=[1,"abc","abc",1]
d_list=c_list.copy()
d_list.reverse()
if(c_list==d_list):
    print("Palindrome")
else:
    print("Not Palindrome") """

#IN CASE OF STRING-

""" a="radar"
if(a==a[::-1]):
    print("Palindrome")

else:
    print("Not palindrome") """

#TUPLE EXERCISE-
#WAP to count the number of students with the 'A' grade in the following tuple.

my_tuple=("C","D","A","A","B","B","A")
print("Number of students who got A is ",my_tuple.count("A"))

#STORE THE ABOVE VALUES IN A LIST & SORT THEM FROM "A TO Z"
my_list=[]
i=0
while(i<7):
    my_list.append(my_tuple[i])
    i=i+1
my_list.sort()
print(my_list)