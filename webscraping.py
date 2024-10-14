import urllib.request, urllib.parse, json, re, math
from bs4 import BeautifulSoup

html=urllib.request.urlopen('https://books.toscrape.com/')
soup=BeautifulSoup(html,'html.parser')
# print(soup.prettify())
# tags=soup.find('ul',class_="nav nav-list")
# lsttag=tags.find_all('li')
# for tag in lsttag:
#     t=tag.find('a')
#     print(t.string.strip())
#     print(t.get('href',None))

#Get all the books information-
# tags=soup.find_all('article',class_="product_pod")
# for tag in tags:
#     t=tag.find('h3')
#     p=tag.find('p',class_="price_color")
#     star=tag.find('p',class_="star-rating")
#     availability=tag.find('p',class_="instock availability")
#     # print(t.string)
#     a=t.find('a')
#     print(f"Book Name: {a.get('title',None)}")
#     print(f"Price: {p.text}")
#     print(f"Rate:{star.get("class",None)[1]} Stars")
#     print(f"Availability:{availability.text.strip()}")

# print(lsttag[2])

# t=lsttag[1].find('a')
# print(t.string.strip())
# print(t.get('href',None))

#Searching link sorting by name-
# bookname=input('Search for the genre: ')
# tags=soup.find('ul',class_="nav nav-list")
# lsttag=tags.find_all('li')
# found=False
# for tag in lsttag:
#     t=tag.find('a')
#     if bookname.capitalize()==t.string.strip():
#         print(t.get('href',None))
#         found=True

# if not found:
#     print("Not found!")

#Searching for a book and it's price and availability by it's genre-
bookname=input('Search for the genre: ')
tags=soup.find('ul',class_="nav nav-list")
lsttag=tags.find_all('li')
found=False
for tag in lsttag:
    t=tag.find('a')
    if bookname.capitalize()==t.string.strip():
        url=t.get('href',None)
        url='https://books.toscrape.com/'+url
        print(url)
        html=urllib.request.urlopen(url)
        soup=BeautifulSoup(html,'html.parser')
        # print(soup.prettify())
        seltags=soup.find_all('article',class_="product_pod")
        print("These are all the books under this genre- ")
        for tag in seltags:
            t=tag.find('h3')
            name=t.find('a')
            price=tag.find('p',class_="price_color")
            stock=tag.find('p',class_="instock availability")
            star=tag.find('p',class_="star-rating")
            print(f"Name: {name.get('title',"N/A")}")
            print(f"Price: {price.string}")
            print(f"Rate: {star.get("class")[1]}")
            print(f"Avalability: {stock.text.strip()}")
            print("\n")
        found=True

if not found:
    print("Not found!")

selectedBook=input('Tell me the book name you are looking for? ').strip().lower()
for tag in seltags:
    t=tag.find('h3')
    name=t.find('a')
    getName=name.get('title',"N/A")
    stock=tag.find('p',class_="instock availability")
    price=tag.find('p',class_="price_color")
    if getName.lower()==selectedBook:
        bookPrice=re.findall(r'£(\d+.+)',price.string)[0]
        print(f"Availability: {stock.text.strip()} and the price is £{bookPrice}")
        print('Do you want to buy this book?(y/n)')
        decision=input('').strip() 
        if decision.lower()=='y':
            proceed=input('Proceed to checkout?(y/n) ').strip()
            if proceed.lower()=='y':
                username=input("Your name: ").strip()
                email=input("Enter your email: ").strip()
                password=input("Enter your password: ").strip()
                found=False
                user_lst=list()
                with open('bankinguserids.txt','r') as f:
                    for line in f:
                        user_infos=json.loads(line)
                        if user_infos['username']==username.lower() and user_infos['email']==email:
                            if user_infos['balance']>=float(bookPrice):
                                print("Your purchase has been completed!")
                                user_infos['balance']-=math.ceil(float(bookPrice))
                        
                            elif  user_infos['balance']<float(bookPrice):
                                print("Insufficient balance in your account!")
                        found=True
                        user_lst.append(user_infos)
                if not found:
                    print("Something went wrong!")
                with open('bankinguserids.txt','w') as fh:
                    for user in user_lst:
                        fh.writelines(json.dumps(user)+'\n')

        else:   
            quit()