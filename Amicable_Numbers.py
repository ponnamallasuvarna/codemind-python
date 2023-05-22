n=int(input())
m=int(input())
sum=0
add=0
for i in range(1,n+1):
    if n%i==0:
        sum=sum+i
for j in range(1,m+1):
    if m%j==0:
        add=add+j
if sum==add:
    print("Amicable")
else:
    print("Not Amicable")