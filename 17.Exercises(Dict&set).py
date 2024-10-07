#Store following word meanings in a Python dictionary.
#table:"a piece of furniture","list of facts & figures." cat:"a small animal"
""" a_dict={
    "table":["a piece of furniture", "list of facts & figures"],
    "cat":"a small animal"
}
print(type(a_dict))
print(a_dict)
print(type(a_dict["table"])) """

#2nd Question-
#You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
#"Python","Java","C++","Python","Javascript","Java","Python","Java","C++","C"
#Using SET-
""" A_set={"Python","Java","C++","Python","Javascript","Java","Python","Java","C++","C"}
print("Classrooms needed for each subject are ",len(A_set)) """

#Somewhat complex way to do it-
""" a_set=set()

i=0
while(i<10):
    print(i+1)
    sub=input("Enter subject: ")
    a_set.add(sub.lower())
    i=i+1

print("Classrooms needed for each subject are ",len(a_set)) """

##WAP to enter marks of 3 subjects from the user and store them in a dictionary.Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
""" marks={}
marks.update({"physics":int(input("Enter your marks for physics: "))})
marks.update({"Chemistry":int(input("Enter your marks for Chemistry: "))})
marks.update({"Math":int(input("Enter your marks for Math: "))})
print(marks) """





##Figure out a way to store 9 & 9.0 as separate values in the set. (You can take help of built-in data types)
anew_set={(9,9.0)}
print(anew_set)