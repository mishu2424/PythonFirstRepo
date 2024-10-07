import random
import time
operators=['+','-','*','/']
MIN_VAL=0
MAX_VALUE=9
COUNT=10
def generatemath():
    left=random.randint(MIN_VAL,MAX_VALUE)
    right=random.randint(MIN_VAL,MAX_VALUE)
    operator=random.choice(operators)
    expr= f"{left} {operator} {right}"
    try:
        answer=eval(expr)
        if(str(answer).isdigit()):
            print(f"{expr} ={answer}")
        elif(str(answer).isdecimal()):
            answer="{:.2f}".format(answer)
            print(f"{expr} = {answer}")
        elif(answer<0):
            if(str(answer).isdecimal()):
                print(f"{expr} = {round(answer,2)}")
            elif(str(answer).isdigit()):
                print(f"{expr} = {answer}")
    except ZeroDivisionError as e:
        print(f"{e} is undefined")
    return expr,answer  
input("Do you wanna start the game?(y/n)")  
start_time=time.time()
for i in range(COUNT):
    print(f"Question {i+1}: ",end="")
    expr,answer=generatemath()
    while True:
        guess=input(f"Result for {expr} is = ")
        if(guess==str(answer)):
            print("Correct!")
            break
        else:
            print("Incorrect! Try again")

end_time=time.time()
final_time=round(end_time-start_time,2)
print(f"Nice work! You finished in {final_time} seconds")
