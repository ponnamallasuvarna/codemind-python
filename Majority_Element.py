n=int(input())
lst=list(map(int,input().split()))
for i in lst:
    if lst.count(i)>n//2 and lst.count(i)!=1:
        print(i)
        break