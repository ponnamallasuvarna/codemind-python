n=int(input())
temp=n
p=n*n
sum=0
while p!=0:
    r=p%10
    sum=sum+r
    p=p//10
if sum==n:
    print("Neon Number")
else:
    print("Not Neon Number")