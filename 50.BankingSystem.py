import hashlib
import json
import re
# 1. User Authentication
user_lst=list()
def hash_password(password):
    """Hashes the password for security."""
    return hashlib.sha256(password.encode()).hexdigest()
def register():
    username=input("Enter your username: ").strip()
    while True:
        email=input("Enter your email address: ").strip()
        if re.match('[a-z]+[0-9]*@(?:gmail|yahoo)\.com',email):
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
        if not re.match('(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}',password):
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
            if user_infos['username'] == username and user_infos['password'] == password and user_infos['email'] == email:
                print(f"Hello {username}")
                user_found=True
        if not user_found:
            print("You don't exist in our system.")
            print('Forget password?(y/n)')
            fp=input().strip().lower()
            if fp=='y':
                while True:
                    emailconfirmation=input('Write your email: ')
                    if re.match('[a-z]+[0-9]*@(?:gmail|yahoo)\.com',emailconfirmation):
                        break
                    else:
                        print("Please enter a valid email address")
                
                with open('bankinguserids.txt','r') as file :
                    for line in file:
                        line=line.strip()
                        try:
                            user_infos=json.loads(line)
                        except:
                            print("Something went wrong! ")
                            continue
                        if user_infos['email'] == emailconfirmation:
                            print("Email verified!")


def authentication():
    print("Welcome to RBC Bank.")
    print('Sign up')
    print('Log in')
    print('Exit')
    user_choice=input().strip().lower()
    if (user_choice=='sign up'):
        if register():
            print("Registration has been sucessful")
    if(user_choice=='log in'):
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