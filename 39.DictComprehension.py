#Dictionary Comprehension
#Syntax--> dictionary = {key: value for vars in iterable}
""" 
Example 1: Dictionary Comprehension
Consider the following code:
square_dict = dict()
for num in range(1, 11):
    square_dict[num] = num*num
print(square_dict)
Now, let's create the dictionary in the above program using dictionary comprehension-

square_dict={num:num*num for num in range(1,11)}
print(square_dict)
"""


# Example 3: How to use Dictionary Comprehension
#item price in dollars
""" old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}

new_price={item:value*12 for (item,value) in old_price.items()}
print(new_price) """

# Example 4: If Conditional Dictionary Comprehension
""" original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

even_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 0}
print(even_dict) """

# Example 5: Multiple if Conditional Dictionary Comprehension
""" original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

new_dict = {k: v for (k, v) in original_dict.items() if v % 2 != 0 if v < 40}
print(new_dict) """

# Example 6: if-else Conditional Dictionary Comprehension
""" original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

selected_persons={name:('old' if age>40 else 'young') for (name,age) in original_dict.items()}
print(selected_persons)
 """
# Example 7: Nested Dictionary with Two Dictionary Comprehensions
""" dictionary = {
    k1: {k2: k1 * k2 for k2 in range(1, 6)} for k1 in range(2, 5)
}
print(dictionary) """
