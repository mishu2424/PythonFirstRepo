#Finding the second largest-
""" n = int(input())
arr = set(map(int, input().split()))
arr=list(arr)
arr.sort(reverse=True)
print(arr[1]) """
arr=[]
for _ in range(int(input())):
       name = input()
       score = float(input())
       arr.extend([(name,score)])
arr.sort(key=lambda score:score[1],reverse=True)
sliced_arr=arr[1:3]
sliced_arr.sort(key=lambda name:name[0])
print()

