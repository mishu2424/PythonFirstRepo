#Project Pig
""" import random

def rollDice():
    totalNumber=0
    roll_diced_one=0
    while(not roll_diced_one):
        choice=input("Would you like to roll a dice?(y)")
        if(choice=='y'):
          number=random.randint(1,6)
          if(number==1):
            totalNumber=0
            print(f"The roll diced {number}")
            print("Your total score is 0!")
            roll_diced_one=1
          else:
            totalNumber+=number
            print(f"The roll diced {number}")
            print(f"Your total number is {totalNumber}")
            if(totalNumber==50):
             print(f"You are the winner!")
             return
        if(choice=='n'):
           print(f"your total number is {totalNumber}.")
           print("____GAME OVER____")
           break
rollDice() """

##NOW FOR MULTIPLE PLAYERS
""" import random

def rollDice():
    diced_value=random.randint(1,6)
    return diced_value

while True:
    players=input("How many players do you want to play with?(2-4)")
    if players.isdigit():
        players=int(players)
        if 2<=players<=4:
            break
        else:
            print("Players must be between 2-4")
    else:
        print("Invalid! Try again.")

players_scores=[0 for _ in range(players)]
print(players_scores)

while max(players_scores) < 20 :
    for player_idx in range(players):
        print(f"\nPlayer {player_idx+1} has just started!\n")
        print("Your total score is",players_scores[player_idx])
        totalScore=0
        while True:
            
            should_roll=input("Would you like to roll the dice?(y)")
            if(should_roll.lower()!='y'):
                break
            value=rollDice()
            if value==1:
                print(f"You rolled a {value}! Turn done!")
                players_scores[player_idx]=0
                totalScore=0
                break
            else:
                totalScore+=value
                print(f"You rolled {value}")
                print("Total {}".format(totalScore))


        players_scores[player_idx]+=totalScore
        print(f"Your total score is {players_scores[player_idx]}")

max_score=max(players_scores)
winning_idx=players_scores.index(max_score)
print(f"Player {winning_idx+1} is the winner") """

""" import random

def rollDice():
    return random.randint(1, 6)

# Get number of players
while True:
    players = input("How many players do you want to play with? (2-4) ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Players must be between 2-4.")
    else:
        print("Invalid input! Please enter a number.")

# Initialize player scores
players_scores = [0 for _ in range(players)]
print(players_scores)

# Game loop
while max(players_scores) < 20:
    for player_idx in range(players):
        print(f"\nPlayer {player_idx + 1} has just started!")
        print("Your total score is", players_scores[player_idx])
        totalScore = 0

        while True:
            should_roll = input("Would you like to roll the dice? (y/n) ")
            if should_roll.lower() != 'y':
                break

            value = rollDice()
            if value == 1:
                print(f"You rolled a {value}! Turn done! Your score for this turn is reset.")
                totalScore = 0  # Reset turn score only
                break
            else:
                totalScore += value
                print(f"You rolled {value}. Total score for this turn: {totalScore}")

        players_scores[player_idx] += totalScore
        print(f"Your total score is now {players_scores[player_idx]}")

# Determine the winner
max_score = max(players_scores)
winning_idx = players_scores.index(max_score)
print(f"Player {winning_idx + 1} is the winner!") """

   
   

import random

def rollDice():
    return random.randint(1,6)
while True:
    player=input("How many players do you want to play with(2-4) ? ")
    if(player.isdigit()):
        player=int(player)
        if(2<=player<=4):
            break
        else:
            print("Players must be between 2 and 4")
    else:
        print("Invalid! Try again")

players=[0 for _ in range(player)]
print(players)

while max(players) <20 :
    for player_idx in range(player):
        print(f"Player {player_idx+1} has started")
        print(f"Your Total score is {players[player_idx]}")
        totalScore=0
        while True:
            decision=input("Would you like to roll a dice?(y/n)")
            if(decision=='n'):
                if(max(players)>20):
                    # exit() #exit function ends the program
                    quit()
                break
            if(decision=='y'):
                value=rollDice()
                if(value==1):
                    print(f"You rolled a {value}. Turn over!")
                    totalScore=0
                    players[player_idx]+=totalScore
                    break
                else:
                    totalScore+=value
                    print(f"You rolled {value}.Your total value is {totalScore}")
        players[player_idx]+=totalScore
        print(f"Your total score is {players[player_idx]}")

maximum=max(players)
print(f"The winner is player no {players.index(maximum)+1}")