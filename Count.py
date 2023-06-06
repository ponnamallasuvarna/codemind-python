n=int(input())
lst=list(map(int,input().split()))
a=0
b=0
for i in lst:
    if i%2==0:
        a+=1
    else:
        b+=1
print(a,b)