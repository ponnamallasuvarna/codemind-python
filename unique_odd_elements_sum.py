n=int(input())
s=0
lst=list(map(int,input().split()))
p=set(lst)
for i in p:
    if i%2!=0:
        s=s+i
print(s)