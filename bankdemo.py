import json
email=input('Your email: ')
# user_found=False
user_confirmation=False
user_lst=list()
# with open('bankdemo.txt','r') as file:
#     for line in file:
#         line=line.strip()
#         try:
#             user_infos=json.loads(line)
#             if user_infos['email']==email:
#                 p=input("New password: ")
#                 user_infos['password']=p
#                 print(type(user_infos))
#                 user_found=True
#                 # user_lst.append(user_infos)
#             user_lst.append(user_infos)
#         except:
#             print('something went wrong!')
#             quit()
# if user_found:
#         with open('bankdemo.txt','w') as file:
#           for user in user_lst:
#             file.writelines(json.dumps(user)+ "\n")
with open('bankdemo.txt','r') as file :
    for line in file:
        line=line.strip()
        try:
            user_infos=json.loads(line)
            if user_infos['email'] == email:
                print("Email verified!")
                while True:
                    print("Enter your new password: ")
                    np=input().strip()
                    print("Confirm your password: ")
                    cp=input().strip()
                    if(np==cp):
                        # password=hash_password(np)
                        user_infos['password']=np
                        user_confirmation=True
                        break
            user_lst.append(user_infos)
        except:
            print("Something went wrong! ")
            continue
if user_confirmation:
    with open('bankdemo.txt','w') as file:
        for user in user_lst:
            file.writelines(json.dumps(user)+"\n") 
        print("Password has been changed!")
# import json
# import hashlib

# def hash_password(password):
#     return hashlib.sha256(password.encode()).hexdigest()

# def update_password(filename):
#     email = input('Your email: ')
#     updated_lines = []
#     user_found = False

#     with open(filename, 'r') as file:
#         for line in file:
#             try:
#                 user_info = json.loads(line.strip())
#                 if user_info['email'] == email:
#                     new_password = input("New password: ")
#                     user_info['password'] = hash_password(new_password)
#                     user_found = True
#                 updated_lines.append(json.dumps(user_info) + "\n")
#             except json.JSONDecodeError:
#                 print(f"Skipping invalid JSON line: {line.strip()}")
#     print(updated_lines)

#     if user_found:
#         with open(filename, 'w') as file:
#             file.writelines(updated_lines)
#         print("Password updated successfully.")
#     else:
#         print("User not found.")

# update_password('bankdemo.txt')