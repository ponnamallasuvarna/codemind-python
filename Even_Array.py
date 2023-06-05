n=int(input())
lst=list(map(int,input().split()))
a=0
for i in lst:
    if i%2==0:
        a=a+1
if a==n:
    print("True")
else:
    print("False")