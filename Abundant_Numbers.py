n=int(input())
sum=0
temp=n
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum>temp:
    print("True")
else:
    print("False")