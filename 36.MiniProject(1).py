#Guess a random number
import random
number=random.randint(1,100)
print(number)
matched=0
try_count=5
print("Welcome to the Guess the Number game!")
print("I have selected a number between 1 and 100.")
print("You have 5 attempts to guess it correctly.")
name=input("Your name: ")
while(not matched):
    if(try_count==2):
        print(f"You are left with {try_count} more trails!")
        decision=input("Do you want to Continue or Quit(Q)?")
        try:
             if(decision.upper()=='Q'):
                quit()
        except:
                print("something went wrong!")
    if(try_count==0):
        print(f"You are out of the game {name}!",end=" ")
        print("Sorry try it some other time!")
        break
    try:
        n=int(input("Guess a number"+ " between (1-100): "))

    except:
        print("Please Enter a valid integer number")
        continue
    if(n==number):
        print(f"You guessed it right! Great job {name}!")
        matched=1
    else:
        if(n>number):
            print("Your guessed number is bigger than the actual number! Try again")
        if(n<number):
            print("Your guessed number is smaller than the actual number! Try again")
        try_count-=1
        print(f"You have {try_count} more trials left")
print("______GAME OVER_____")