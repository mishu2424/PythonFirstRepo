import urllib.request, urllib.parse, json
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
        tags=soup.find_all('article',class_="product_pod")
        for tag in tags:
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