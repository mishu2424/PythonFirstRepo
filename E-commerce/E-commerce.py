import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, json, re, time, math
from bs4 import BeautifulSoup
import hashlib
import sqlite3

# 1. User Authentication
user_lst=list()
def hash_password(password):
    """Hashes the password for security."""
    return hashlib.sha256(password.encode()).hexdigest()
authentication_confirmation=False
def register():
    global authentication_confirmation
    username=input("Enter your username: ").strip().lower()
    while True:
        email=input("Enter your email address: ").strip()
        if re.match(r'[a-z]+[0-9]*@(?:gmail|yahoo)\.com',email):
            break
        else:
            print("Please enter a valid email address!")
    with open('bankdemo.txt','r') as file:
        for data in file:
            if username in data and email in data:
                 print("You are already registered!")
                 return
    # OR
    # with sqlite3.connect('storeinfodb.sqlite') as conn:
    #         cur = conn.cursor()
    #         cur.execute("SELECT * FROM Users WHERE username = ? OR email = ?", (username, email))
    #         if cur.fetchone():
    #             print("Username or email already exists. Please choose another.")
    #             continue
    #         break
    
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
    with open('E-commerce/users.txt','a') as file:
        file.writelines(json.dumps(new_user) + "\n")
        authentication_confirmation=True
    return True       
def signin():
    global authentication_confirmation
    user_found=False
    user_confirmation=False
    user_lst=list()
    username=input("Enter your name: ").strip()
    email=input("Enter your email: ").strip()
    password=input("Enter your password: ").strip()
    password=hash_password(password)
    with open('E-commerce/users.txt','r') as file :
        for line in file:
            line=line.strip()
            try:
                user_infos=json.loads(line)
            except:
                print("Something went wrong! ")
                continue
            if user_infos['username'] == username.lower() and user_infos['password'] == password and user_infos['email'] == email:
                print(f"Hello {username}")
                authentication_confirmation=True
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
                
                with open('E-commerce/users.txt','r') as file :
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
                    with open('E-commerce/users.txt','w') as file:
                        for user in user_lst:
                            file.writelines(json.dumps(user)+"\n") 
                            authentication_confirmation=True
                        print("Password has been changed!")
    if user_found:
        return True        
                                        
# 225b9366ba83b2aee70ab1d37b3f69996a3411ed111eb1f5de5d94d9aed5811e

def authentication():
    print('Sign up')
    print('Sign in')
    print('Exit')
    user_choice=input().strip().lower()
    if (user_choice=='sign up'):
        if register():
            print("Registration has been sucessful")
            return True
    if(user_choice=='sign in'):
        if signin():
            return True
    if(user_choice=='exit'):
        quit()


# def storeInfodb():
#     with sqlite3.connect('storeinfodb.sqlite') as conn:
#         cur = conn.cursor()
#         cur.executescript('''
#             DROP TABLE IF EXISTS Users;
#             CREATE TABLE Users (
#                 id INTEGER PRIMARY KEY,
#                 name TEXT UNIQUE,
#                 email TEXT UNIQUE,
#                 password TEXT
#             )
#         ''')

#     with open('E-commerce/users.txt','r') as users:
#         for user in users:
#             user=user.strip()
#             user_infos=json.loads(user)
#             name=user_infos['username']
#             email=user_infos['email']
#             password=user_infos['password']
#             cur.execute('''INSERT OR IGNORE INTO Users (name, email, password)
#             VALUES ( ?, ?, ? )''', ( name,email,password ) )
#             conn.commit()
#     cur.close()
# storeInfodb()
def home_menu():
    global authentication_confirmation
    print("Here are all the products:")
    tree=ET.parse('E-commerce/README.xml')
    print(tree)
    root=tree.getroot()
    products=root.find('products')
    for product in products:
        print(f"Product : {product.find('name').text}")
        print(f"Description : {product.find('description').text}")
        print(f"Price : {product.find('price').text}")
        print(f"Category : {product.find('category').text}")
        if int(product.find('stock').text) > 0:
            print("Stock : Available")
        else:
            print("Stock : Not available")
        print('\n')

    print('Here are all the categories: ') 

    categories=root.find('categories')
    for category in categories:
        print(category.get('name'))
    cat=input('Tell me the category: ').lower().strip()
    for category in categories:
        if category.get('name').lower()==cat:
            url=category.get('link')
            url=url.replace('https://example.com/','http://localhost:8000/')+'.html'
            print(url)
            html=urllib.request.urlopen(url)
            soup=BeautifulSoup(html,'html.parser')
            # print(soup.prettify())
            print('Here are all the items under this category: ')
            product_list=list()
            orders_list=list()
            user_decision=True
            tags=soup.find('ul')
            lsttag=tags.find_all('li')
            for tag in lsttag:
                print(f"Product : {tag.find('h2').string}")
                print(f"Description: {tag.find('p', class_="Description").text}")
                print(f"{tag.find('p',class_="price").text}")
                # product_list.append()
            while user_decision:
                user_choice=input('Do you want to buy(y/n)? ')
                if user_choice=='y':
                    if authentication_confirmation:
                        product=input('').strip().lower()
                        for tag in lsttag:
                            product_name=tag.find('h2').string
                            if product==product_name.lower():
                                price=tag.find('p',class_="price").text
                                price=re.findall(r'\$(\d+\.\d+)',price)
                                print('Product has been added to cart ')
                                orderdict={
                                    'name':product_name,
                                    'Price':price[0]
                                }
                                print(orderdict)
                                orders_list.append(orderdict)
                    if not authentication_confirmation:
                        if authentication():
                             product=input('').strip().lower()
                             for tag in lsttag:
                                 product_name=tag.find('h2').string
                                 if product==product_name.lower():
                                     price=tag.find('p',class_="price").text
                                     price=re.findall(r'\$(\d+\.\d+)',price)
                                     print('Product has been added to cart ')
                                     orderdict={
                                         'name':product_name,
                                         'Price':price[0]
                                     }
                                     print(orderdict)
                                     orders_list.append(orderdict)
                if user_choice=='n':
                    user_decision=False       
    with open('E-commerce/orders.txt','a') as fh:
        print('hello')
        for order in orders_list:
            print(type(order))
            fh.writelines(json.dumps(order)+'\n')
print('Welcome to MiniBazar')
print('Do you want to sign in or sign up?(y/n)')
user_dec=input('').lower().strip()
if user_dec=='y':
    if authentication():
        home_menu()
elif user_dec=='n':
    home_menu()

