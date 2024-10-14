import hashlib
import json
import re
# 1. User Authentication
user_lst=list()
def hash_password(password):
    """Hashes the password for security."""
    return hashlib.sha256(password.encode()).hexdigest()
def register():
    username=input("Enter your username: ").strip().lower()
    address=input("Enter your address: ")
    while True:
        phone_number=input("Enter your phone number: +1")
        phone_number="+1 "+phone_number
        phone_number=phone_number.replace(' ','')
        print(len(phone_number))
        if len(phone_number)==12 and re.match(r'\+1\d.+',phone_number):
            break 
    while True:
        sin_no=input('Enter your SIN: ')
        if (len(sin_no)==4) and sin_no.isdigit():
            break
    while True:
        email=input("Enter your email address: ").strip()
        if re.match(r'[a-z]+[0-9]*@(?:gmail|yahoo)\.com',email):
            break
        else:
            print("Please enter a valid email address!")
    with open('bankinguserids.txt','r') as file:
        for data in file:
            if username in data and email in data:
                 print("You are already registered!")
                 return 
    while True:
        print("1.At least one lowercase letter (a-z)\n2.At least one uppercase letter (A-Z)\n3.At least one digit (0-9)\n4.At least one special character (e.g., !@#$%^&*)\5.A minimum length (e.g., 8 characters)\n")
        password=input("Enter your pass: ").strip()
        if not re.match(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}',password):
            print("Password pattern didn't match")
        else:
            break
    password=hash_password(password)
    print(password)
    new_user = {
        'username': username,
        'email': email,
        'address':address,
        'phone_no':phone_number,
        'sin_no':sin_no,
        'balance':0,
        'password': password
    }
    user_lst.append(new_user)
    print(user_lst)
    with open('bankinguserids.txt','a') as file:
        file.writelines(json.dumps(new_user) + "\n")
    return True       
def signin():
    user_found=False
    user_confirmation=False
    user_lst=list()
    username=input("Enter your name: ").strip()
    email=input("Enter your email: ").strip()
    password=input("Enter your password: ").strip()
    password=hash_password(password)
    # with open('bankinguserids.txt','r') as file :
    #     for line in file:
    #         if username in line and password in line:
    #             print(f"Hello {username}")
    #             user_found=True
    #     if not user_found:
    #         print("You don't exist in our system.")
    with open('bankinguserids.txt','r') as file :
        updatedinfos=list()
        for line in file:
            line=line.strip()
            try:
                user_infos=json.loads(line)
            except:
                print("Something went wrong! ")
                continue
            if user_infos['username'] == username.lower() and user_infos['password'] == password and user_infos['email'] == email:
                print(f"Hello {username}")
                # current_balance=user_infos['balance']
                while True:
                    print(f"Your current balance is {user_infos['balance']}")
                    print("1.Deposit")
                    print("2.Withdraw")
                    print("3.History")
                    print("4.Exit")
                    user_choice=input('')
                    if user_choice=='1' or user_choice.lower().strip()=='deposit':
                        print("Enter the amount you want to deposit: ")
                        while True:
                            depositted_money=input('')
                            try:
                                depositted_money=int(depositted_money)
                                break
                            except:
                                print("Invalid input!")
                                continue
                            
                        user_infos['balance']+=depositted_money
                        print(f"Your current balance is {user_infos['balance']}")
                    if user_choice=='2' or user_choice.lower().strip()=='withdraw':
                        print("Enter the amount you want to deduct: ")
                        while True:
                            deducted_money=input('')
                            try:
                                deducted_money=int(deducted_money)
                                break
                            except:
                                print("Invalid input!")
                                continue
                        if user_infos['balance'] >= deducted_money: 
                            user_infos['balance']-=deducted_money 
                            print(f"Your current balance is {user_infos['balance']}")
                        elif user_infos['balance'] < deducted_money:print("Insufficicent balance!")
                    if user_choice=='3' or user_choice.lower().strip()=='history':
                        with open('transactions.txt','r') as filehandle:
                            for line in filehandle:
                                user_datas=json.loads(line)
                                if user_datas['email']==email and user_datas['username']==username.lower():
                                    print("Your transactions:")
                                    print(f"{user_datas['description']} Time:{user_datas['time']}")


                    if user_choice=='4' or user_choice.lower().strip()=='exit':
                        break
                user_found=True
                
            updatedinfos.append(user_infos)
           
        
        with open('bankinguserids.txt','w') as fhandle:
            for info in updatedinfos:
                fhandle.writelines(json.dumps(info)+'\n')
            # return True
        if not user_found:
            print("You don't exist in our system.")
            print('Forget password?(y/n)')
            fp=input().strip().lower()
            if fp=='y':
                while True:
                    emailconfirmation=input('Write your email: ')
                    if re.match(r'[a-z]+[0-9]*@(?:gmail|yahoo)\.com',emailconfirmation):
                        break
                    else:
                        print("Please enter a valid email address")
                
                with open('bankinguserids.txt','r') as file :
                    for line in file:
                        line=line.strip()
                        try:
                            user_infos=json.loads(line)
                            if user_infos['email'] == emailconfirmation:
                                print("Email verified!")
                                while True:
                                    while True:
                                        print("1.At least one lowercase letter (a-z)\n2.At least one uppercase letter (A-Z)\n3.At least one digit (0-9)\n4.At least one special character (e.g., !@#$%^&*)\5.A minimum length (e.g., 8 characters)\n")
                                        print("Enter your new password: ")
                                        np=input().strip()
                                        if re.match(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}',password):
                                            break
                                    print("Confirm your password: ")
                                    cp=input().strip()
                                    if(np==cp):
                                        # password=hash_password(np)
                                        user_infos['password']=hash_password(np)
                                        user_confirmation=True
                                        break
                            user_lst.append(user_infos)
                        except:
                            print("Something went wrong! ")
                            continue
                if user_confirmation:
                    with open('bankinguserids.txt','w') as file:
                        for user in user_lst:
                            file.writelines(json.dumps(user)+"\n") 
                        print("Password has been changed!")
                        return True
    return True                                     
# 225b9366ba83b2aee70ab1d37b3f69996a3411ed111eb1f5de5d94d9aed5811e

def authentication():
    print("Welcome to Barsha Bank.")
    print('Sign up')
    print('Sign in')
    print('Exit')
    user_choice=input().strip().lower()
    if (user_choice.lower().replace(' ','')=='signup'):
        if register():
            print("Registration has been sucessful")
            return 'registered'
        else:
            signin()
    if(user_choice.lower().replace(' ','')=='signin'):
        if signin():
            return 'signedin'
    if(user_choice=='exit'):
        quit()

status=authentication()
if status=='registered':
    print("Do you want to see your balance/deposit/withdraw?(y/n)")
    bal=input('')
    if bal=='y':
        signin()    
    if bal=='n':
        quit()
    else:
        quit()

if status=='signedin':
    print("Thank you for banking with us")
# with open('bankinguserids.txt','r') as file:
#     for line in file:
#         line=line.strip()
#         if line:
#             name=json.loads(line)
#             print(type(name))
#             print(name['username'])