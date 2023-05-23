n=int(input())
ct=0
for i in range(1,n+1):
    if n%i==0:
        ct=ct+1
if ct==2:
    print("prime")
else:
    print("not a prime")
   