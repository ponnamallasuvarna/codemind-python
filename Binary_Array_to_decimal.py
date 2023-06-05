n=int(input())
lst=list(map(int,input().split()))
i=1
a=0
b=0
for i in lst[::-1]:
    m=i*2**a
    b=b+m
    a=a+1
print(b)