#Calculator Project
def user_input():
    while True:
        number1 = input("Enter the first value: ")
        number2 = input("Enter the second value: ")

        # Check if both inputs are valid numbers (including negative and decimal)
        try:
            number1 = float(number1)
            number2 = float(number2)
            return number1,number2
         
        except ValueError:
            print("Invalid! Please enter valid numeric values.")

reservedValue=[]
operators='+-*/%^'
count_operation=0
def sum(number1,number2):
    plusValue=number1+number2
    # print(type(plusValue))
    reservedValue.append(plusValue)
    return plusValue

def subtraction(number1,number2):
    minusValue=number1-number2
    reservedValue.append(minusValue)
    return minusValue

def multiplication(number1,number2):
    multiValue=number1*number2
    reservedValue.append(multiValue)
    return multiValue

def division(expr):
    divValue=eval(expr)
    print("{:.2f}".format(divValue))
    reservedValue.append(divValue)

def modulus(expr):
    moduValue=eval(expr)
    print(moduValue)
    reservedValue.append(moduValue)

def power(number1,number2):
    powValue=number1 ** number2
    reservedValue.append(powValue)
    return powValue
    

def continuing_operations(totalValue):
    while True:
        decision=input("Would you like to continue doing operations with the previous number?(y/n) ")

        if(decision.lower()=='y'):
            while True:
                new_Number=input("Enter a new number: ")
                try:
                    new_Number=float(new_Number)
                    break
                except:
                    print("Invalid number!")
            operator=input("Choose one of these operators(+-*/%^): ")
            expr=f"{totalValue}{operator}{new_Number}"
            if(operator in operators):
                if(operator=='+'):
                    total=sum(totalValue,new_Number)
                    print(f"{expr}={total}")
                    totalValue+=new_Number
                if(operator=='-'):
                    sub=subtraction(totalValue,new_Number)
                    print(f"{expr}={sub}")
                    totalValue-=new_Number
                if(operator=='*'):
                    multiValue=multiplication(totalValue,new_Number)
                    print(f"{expr}={multiValue}")
                    totalValue=totalValue*new_Number
                if(operator.lower()=='^'):
                    powValue=power(totalValue,new_Number)
                    print(f"{expr}={powValue}")
                    totalValue=powValue
        if(decision.lower()=='n'):
            break

def storing_history(expr,value):
    with open("calculator.txt","w") as f:
        f.write(f"{expr}={value}")
    showing_history()

def showing_history():
    with open("calculator.txt","r") as f:
        data=f.read()
        print("Stored informations in the file- ",data)  
        while True:  
            ask_del=input("Do you want to delete the history?(y/n)")
            if(ask_del.lower()=='y'):
                with open("calculator.txt","w"):
                    pass #Clears the file
                    data=f.read()
                    
                    print("History has been deleted!")
                    break

            elif(ask_del.lower()=='n'):
                break
            else:
                print("Invalid input!")

def operations(number1,number2):
    totalValue=0
    while True:
            operator=input("Choose one of these operators(+-*/%^): ")
            expr=f"{number1}{operator}{number2}"
            # print(type(expr))
            if(operator in operators):
                if(operator=='+'):
                    total=sum(number1,number2)
                    print(f"{expr}={total}")
                    storing_history(expr,total)
                    totalValue=totalValue+total
                    continuing_operations(totalValue)
                if(operator=='-'):
                    sub=subtraction(number1,number2)
                    print(f"{expr}={sub}")
                    totalValue=sub-totalValue
                    continuing_operations(totalValue)
                if(operator=='*'):
                    mutliValue=multiplication(number1,number2)
                    print(f"{expr}={mutliValue}")
                    totalValue=totalValue*mutliValue
                    continuing_operations(totalValue)
                if(operator=='/'):
                    try:
                        division(expr)
                    except ZeroDivisionError:
                        print("Undefined")
                if(operator=='%'):
                    modulus(expr)
                if(operator.lower()=='^'):
                    powerValue=power(number1,number2)
                    print(f"{expr}={powerValue}")
                    totalValue=powerValue
                    continuing_operations(totalValue)

                break
            else:
                print("Invalid operators! Choose a valid one")
    
while True:
    if(count_operation==0):
        number1,number2=user_input()
        operations(number1,number2)
        count_operation=1
    if(count_operation):
        choice=input("Do you want to operate new operations?(y/n) ")
        if(choice=='y'):
                number1,number2=user_input()
                operations(number1,number2)
        if(choice=='n'):
            break
stored_value=input("Do you want to see the history?(y/n) ")
if(stored_value=='y'):
  
    print("History", ",".join([str(value) for value in reservedValue ]))
    delt=input("\nDo you want to delete the history?(y/n) ")
    if(delt=='y'):
        reservedValue.clear()
        print("History has been deleted!")
    else:
        print("Thank you for using me! See you later")

if(stored_value=='n'):
    delt=input("Do you want to delete the history?(y/n) ")
    if(delt=='y'):
        reservedValue.clear()
        print("History has been deleted!")
    else:
        print("Thank you for using me! See you later")
