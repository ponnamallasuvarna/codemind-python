n=int(input())
li=list(map(int,input().split()))
l=set(li)
s=0
for i in l:
    if i%2==0:
        s+=i
print(s)