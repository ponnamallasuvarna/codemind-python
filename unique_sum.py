n=int(input())
lst=list(map(int,input().split()))
a=set(lst)
b=0
for i in a:
    b=b+i
print(b)