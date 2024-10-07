##Define a Circle Class to create a circle with radius r using the constructor.
#Define an Area() method of the class which calculates the area of the  circle.
#Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.
""" class Circle:
    def __init__(self,radius):
        self.radius=radius
    def Area(self):
        return f"The area of the square is {3.14*(self.radius)**2}"
    def Perimeter(self):
        return f"The perimeter of the circle is {2*3.14*(self.radius):.2f}"
circle=Circle(5)
print(circle.Area())
print(circle.Perimeter()) """

##Define a Employee class with attributes role,department & salary. This class also has a showDetails() method.
#Create an Engineer class that inherits properties from Employee & has additional attributes: name & age.

""" class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary

    def showDetails(self):
        ##3 ways of concatenation
        print("Your role is "+self.role)
        print(f"Your department is {self.department}")
        print("Your salary is {}".format(self.salary))

class Engineer(Employee):
    def __init__(self,role,department,salary,name,age):
        super().__init__(role,department,salary)
        self.name=name
        self.age=age
    def showDetailsOfEngineer(self):
        print (f"Your name is {self.name}")
        print (f"Your name is {self.age}")

        


eng1=Engineer("Junior Developer","Web development","CAD 50000","Apurbo Dey Mishu",24)
eng1.showDetailsOfEngineer()
eng1.showDetails()
 """

##Create a class called Order which stores item and its price.
#Use Dunder function __gt__ to convey that:
      #order1>order2 if price of order1 > price of order2

# class Order:
#     stored_list=[]
#     def __init__(self,item,price):
#         self.item=item
#         self.price=price
#     def showStoredItems(self):
#         Order.stored_list.append({self.item:f"CAD {self.price}$"})
#         return Order.stored_list #To get a list
#         # return {self.item:f"CAD {self.price}$"}    ##To get a dictionary.
#     def __gt__(self,order2):
#         if(self.price>order2.price):
#             return Order(self.item,self.price)
#         else:
#             return Order(order2.item,order2.price)

# order1=Order("Sunglass",100)
# order2=Order("Laptop",2000)

# order3=order1.filtering(order2)
# order3=order1>order2
# print(order3.showStoredItems())
# print(order1>order2)
# print(order1.filtering(order2))


##Another way to do that-
""" class Order:
    
    def __init__(self,item,price):
        self.item=item
        self.price=price    
    def __gt__(self,order2):
        stored_list=[]
        if(self.price>order2.price):
            stored_list.append({self.item:f"CAD {self.price}$"})
            stored_list.append({order2.item:f"CAD {order2.price}$"})

        else:
            stored_list.append({order2.item:f"CAD {order2.price}$"})
            stored_list.append({self.item:f"CAD {self.price}$"})
        return stored_list

order1=Order("Sunglass",100)

order2=Order("Laptop",2000)

order3=order1>order2
print(order3) """
# print(order1>order2)
# print(order1.filtering(order2))

##For multiple orders
class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    @staticmethod
    def compareOrders(order1,order2,order3,order4,order5):
        stored_list=[]
        orders=[order1,order2,order3,order4,order5]
        ##Using lambda function
        orders.sort(key=lambda x:x.price,reverse=True)
        ##Here now if I print orders as a list the output will be something like this-
        # [<__main__.Order object at 0x000002620D236750>, <__main__.Order object at 0x000002620D2368D0>, <__main__.Order object at 0x000002620D2369F0>, <__main__.Order object at 0x000002620D2369C0>, <__main__.Order object at 0x000002620D236780>]
        #It's beacuse when you store objects in a list and print that list, Python uses the default string representation for those objects.
        #Printing Lists of Simple Types:
        # When you print a list of simple data types (like integers or strings), such as
        # a_list = [3, 4, 5, 1]
        # print(a_list)
        #The output will show the list in its exact form:
        # [3, 4, 5, 1]

        # When you print a list of objects (like instances of your Order class), such as
        # orders = [order1, order2, order3]
        # print(orders)
        #Output will be-
        # [<__main__.Order object at 0x7f8e6c0bd250>, <__main__.Order object at 0x7f8e6c0bd290>, ...]
        #Reason for the Difference
        # Simple Types: Python has built-in string representations for basic types (like integers, floats, strings, etc.), which are clear and meaningful.

        # Custom Objects: For custom classes, if you don’t define how instances should be represented, Python will fall back on the default object representation, which isn’t helpful for understanding the content of the objects.

        print(orders) 
        for order in orders:
            stored_list.append({order.item:f"CAD {order.price}$"}) #<-- Storing as a dictionary
            # stored_list.append((order.item,f"CAD {order.price}$")) #<-- Storing as a tuple
        return stored_list
order1 = Order("Sunglass", 100)
order2 = Order("Laptop", 2000)
order3 = Order("Watch", 200)
order4 = Order("TV", 500)
order5 = Order("Microwave", 400)
sorted_orders=Order.compareOrders(order1,order2,order3,order4,order5)
print(sorted_orders)
##Lambda functions-
# A lambda function in Python is a small, anonymous function defined using the lambda keyword.
# It can take any number of arguments but can only have one expression.
#Syntax-->lambda arguments: expression 
#Lambda functions are often used when you need a small function for a short period and do not want to formally define it using the def keyword.
##Some examples of lambda function from chatgpt
# 1. Simple Lambda Function
# A lambda function to add two numbers
""" add = lambda x, y: x + y

# Using the lambda function
result = add(3, 5)
print(result) """  # Output: 8

#2. Lambda with Sorting
# List of tuples (name, age)
""" people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]

# Sort by age
people.sort(key=lambda person: person[1])
print(people) """  # Output: [('Bob', 25), ('Alice', 30), ('Charlie', 35)]
#3. Lambda with Filtering
""" 
Purpose: The filter function is used to select elements from an iterable based on a condition defined in a function.
Usefulness: It's particularly useful for cleaning or processing data by removing unwanted elements according to specific criteria.
"""
#filter() function syntax-->filter(function, iterable)
#A function that tests each element in the iterable to determine if it should be included in the result. This can be a regular function or a lambda function.
#The filter function returns an iterator containing only the elements for which the function returned True.
#list(...): Since filter returns an iterator, wrapping it in list() converts the filtered results back into a list.
# List of numbers
""" numbers = [1, 2, 3, 4, 5, 6]

# Filter out even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]
 """
# 4. Lambda with Map
"""
Transformation: The map function is primarily used for transforming data. You can apply any operation you want, such as converting data types, applying mathematical operations, or even modifying strings.
Efficiency: It can be more efficient than using a list comprehension for large datasets since it processes items one at a time. 
"""
#map() function syntax-->map(function, iterable)
#A function that defines the operation to apply to each element of the iterable. This can be a regular function or a lambda function.
#The map function returns an iterator that yields the results of applying the function to each item in the iterable.
#list(...): Since map returns an iterator, wrapping it in list() converts the results into a list.
# List of numbers
""" numbers = [1, 2, 3, 4, 5]

# Square each number using map and lambda
squared = list(map(lambda x: x ** 2, numbers))
print(squared) """  # Output: [1, 4, 9, 16, 25]
##OR
""" def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))

print(squared_numbers)  """ # Output: [1, 4, 9, 16, 25]

