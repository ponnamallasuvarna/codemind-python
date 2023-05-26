n=int(input())
lst=list(map(int,input().split()))
for i in lst[::-1]:
    if i%2!=0:
        break
print(i)