import random

def play():
    print("How many rounds do you want to play?")
    while True:
        Total_round=input().strip()
        try:
            Total_round=int(Total_round)
            break
        except:
            print("Enter a valid integer number!")
            continue
    # while True:
    #     print("How many players do you wanna play with?")
    player_point,opponent_point=0,0
    while Total_round:
        print("'r for Rock, 'p' for Paper, 's' for Scissor")
        player=input().strip().lower()
        opponent=random.choice(['r','p','s'])
        print(player,opponent)
        if player==opponent:
            print('Tied round')
        if player!=opponent and is_Win(player,opponent):
            player_point=player_point+1
            print("Yaa! You won this round!")
        if player!=opponent and not is_Win(player,opponent):
            opponent_point=opponent_point+1
            print("You lost this round!")
        Total_round-=1

    return player_point,opponent_point
    

def is_Win(player,opponent):
    if (player=='r' and opponent =='s') or \
    (player=='s' and opponent=='p') or \
    (player=='p' and opponent=='r'):
        return True
    else:
        return False

playerpoints,opponentpoints=play()
if(playerpoints==opponentpoints):
    print("The game has been tied!")
elif(playerpoints>opponentpoints):
    print(f"You have won the game by {playerpoints-opponentpoints} points!")
elif(playerpoints<opponentpoints):
    print(f"You have lost the game by {opponentpoints-playerpoints} points!")
    
