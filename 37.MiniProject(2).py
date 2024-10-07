#Random password generator
import random
import string
#ascii meaning American Standard Code for Information Interchange
digits=string.ascii_letters+string.punctuation+string.digits
password=""
for _ in range(12):
    password+=random.choice(digits)
print(password)
#Another way to do it-
# pass_generator=''.join(random.choice(digits) for _ in range(12))
# print(pass_generator)
##Another way to do it-
#Using list comprehension concept of Python
# pass_generator=''.join([random.choice(digits) for _ in range(12)])
# print(pass_generator)

