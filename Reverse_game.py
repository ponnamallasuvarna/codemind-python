def reverse(n):
    rev=0
    while n:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
n=int(input())
lst=list(map(int,input().split()))
l=[]
for i in lst:
    print(reverse(i),end=" ")