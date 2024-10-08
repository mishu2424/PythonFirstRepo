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
        for line in file:
            line=line.strip()
            try:
                user_infos=json.loads(line)
            except:
                print("Something went wrong! ")
                continue
            if user_infos['username'] == username.lower() and user_infos['password'] == password and user_infos['email'] == email:
                print(f"Hello {username}")
                user_found=True
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
                                        
# 225b9366ba83b2aee70ab1d37b3f69996a3411ed111eb1f5de5d94d9aed5811e

def authentication():
    print("Welcome to RBC Bank.")
    print('Sign up')
    print('Sign in')
    print('Exit')
    user_choice=input().strip().lower()
    if (user_choice=='sign up'):
        if register():
            print("Registration has been sucessful")
    if(user_choice=='sign in'):
        signin()
    if(user_choice=='exit'):
        quit()

authentication()
# with open('bankinguserids.txt','r') as file:
#     for line in file:
#         line=line.strip()
#         if line:
#             name=json.loads(line)
#             print(type(name))
#             print(name['username'])