import re

a_string="Elon Mask's phone number is 9991116666, call him if you have any question on dodgecoin. Tesla's revenue is 40 billion.\
Tesla's CFO number is (999)-333-7777"

pattern ="\(\d{3}\)-\d{3}-\d{4}|\d{10}"

matched=re.findall(pattern,a_string)
print(matched)

a_text='abgg:;hgj;guudj-grj$'
pattern2='[^:;$-]'
pattern3='[^:;$-]+'
pattern4='[^a-z]'
pattern5='[^a-z]+'
matched2=re.findall(pattern2,a_text)
print(matched2)
matched3=re.findall(pattern3,a_text)
print(matched3)
print(re.findall(pattern4,a_text))
print(re.findall(pattern5,a_text))

with open('regex1.txt','r') as file:
    text1=file.read()
pattern6='Note \d - [^\n]+'
pattern7="Note \d - ([^\n]+)"
print(re.findall(pattern6,text1))
print(re.findall(pattern7,text1))

text2= '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion. 
'''
pattern8="FY\d{4} Q[1234]|fy\d{4} Q[1-4]"
# OR
pattern9="FY\d{4} Q[1-4]"
pattern10="FY(\d{4} Q[1-4])"
print(re.findall(pattern8,text2))
print(re.findall(pattern9,text2,flags=re.IGNORECASE))
print(re.findall(pattern10,text2,flags=re.IGNORECASE))
pattern11="\$\d [a-z]+"
pattern12="\$[\d\.]+ [a-z]+"
print(re.findall(pattern11,text2))
print(re.findall(pattern12,text2))
pattern13="FY\d{4} Q[1-4]|\$\d\.\d+ [a-z]+"
print(re.findall(pattern13,text2))
pattern14="FY\d{4} Q[1-4]|\$[\d\.]+ [a-z]+"
print(re.findall(pattern14,text2,flags=re.IGNORECASE))
pattern15="FY(\d{4} Q[1-4] [^\$]+\$\d\.\d+ [a-z]+)"
print(re.findall(pattern15,text2))
pattern16="FY(\d{4} Q[1-4] [^\$]+\$[\d\.]+ [a-z]+)"
print(re.findall(pattern16,text2))
pattern17 = 'FY(\d{4} Q[1-4])[^\$]+\$([0-9\.]+)'
print(re.findall(pattern17,text2,flags=re.IGNORECASE))
#search() method just finds the first occurence.
matches = re.search(pattern17, text2)
print(matches.group())

text3='abacadaeaf'
pattern18='a.*?e'
print(re.findall(pattern18,text3))
text4="Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.\
BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion."
pattern19= '\d{4} (?:Q[1-4]|S[1-2])'
print(re.findall(pattern19,text4))
text4='apurbomishu24@gmail.com'
pattern20='[a-z]+\d+@+(?:gmail|yahoo)\.com'
print(re.search(pattern20,text4).group())
text5='apurbomishu24@gmail.com\
apurbomishu@yahoo.com'
pattern21='[a-z]+\d*@(?:gmail|yahoo)\.com'
print(re.findall(pattern21,text5))