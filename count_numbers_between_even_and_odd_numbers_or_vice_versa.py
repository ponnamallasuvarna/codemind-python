n=int(input())
lst=list(map(int,input().split()))
c=0
for i in range(1,len(lst)-1):
    if lst[i-1]%2==0 and lst[i+1]%2!=0 or  lst[i-1]%2!=0 and  lst[i+1]%2==0:
        c=c+1
print(c)
