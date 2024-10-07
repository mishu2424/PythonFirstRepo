##Create a student that takes name & marks of 3 subjects as arguments in constructor. Then create method to print the average.
""" class Student :
    def __init__(self,name,phy_marks,math_marks,chem_marks):
        self.name=name
        self.marks={
            "phy": phy_marks,
            "Math": math_marks,
            "Chem": chem_marks
        }
    def average(self,phy_marks,math_marks,chem_marks):
        return (phy_marks+math_marks+chem_marks)/3

s1=Student("Barsha",98,87,99)
a_list=[s1]
sum=0
if(s1.name=="Barsha"):
    for subject,marks in s1.marks.items():
        print("Subject:",subject,"& Marks:",marks)
        if(marks>90):
            print("You got A+ in",subject)
        elif(marks<90 and marks>=80):
            print("You got A in",subject)
        sum+=marks
    print("Your average score is {:.2f}%".format(sum/3))
    
print(s1.average(98,87,99))
 """
##Another way to do it
class Student :
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        self.average()
    def average(self):
        sum=0
        for i in self.marks:
            sum+=i
        print("Hi",self.name,"Your average score is {:.2f}%".format(sum/3))


s1=Student("Barsha",[98,87,99])
# s1.average()

##Create an Account class with 2 attributes- balance & acc no. Create methods for debit, credit and printing the balance.
class Account:
    def __init__(self,balance,accno):
        self.balance=balance
        self.accno=accno
    def debit(self,debitted_money):
        self.balance-=debitted_money
        print(debitted_money,"has been used for debit")
    def credit(self,creditted_money):
        self.balance+=creditted_money
        print(creditted_money,"has been creditted.")
    def current_balance(self):
        print("Your current balance is",self.balance)
acc1=Account(1000,2356)
acc1.debit(200)
acc1.credit(300)
acc1.current_balance()