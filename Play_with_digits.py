n=int(input())
lst=list(map(int,input().split()))
a=0
for i in lst:
    while(i):
        r=i%10
        a+=r
        i=i//10
print(a)