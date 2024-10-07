##MadlibGenerator
with open("story.txt","r") as f:
    data=f.read()

print(data)
start_of_word=-1
words=set()
for i,char in enumerate(data):
    if(char=="<"):
        start_of_word=i
    if(char==">" and start_of_word!=-1):
        word=data[start_of_word:i+1]
        words.add(word)
        start_of_word=-1
print(words)
answers={}

# """ while True:
#     for word in words:
#         answer=input(f"Enter a word for {word}: ")
#         if(answer.isdigit()):
#             print("Invalid! Try again")
#             continue
#         answers[word]=answer
#     break """


for word in words:
    while True:
        answer=input(f"Enter a word for {word}: ")
        if(answer.isdigit()):
            print("Invalid! Try again")
        else:
            answers[word]=answer
            break

 

for word,newWords in answers.items():
    data=data.replace(word,newWords)
print(data)

