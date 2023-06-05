n=int(input())
lst=list(map(int,input().split()))
a=0
b=set(lst)
for i in b:
    if i%2!=0:
        a=a+1
print(a)