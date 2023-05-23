import math
def isprime(n):
    if n<2:
        return False
    s=int(math.sqrt(n))
    for i in range(2,s+1):
        if n%i==0:
            return False
    return True
        
n=int(input())
p=(isprime(n))
l=[]
while n!=0:
    r=n%10
    l.append(r)
    n=n//10
k=[]
for i in l:
    if isprime(i):
         k.append(i)
if len(k)==len(l)and p:
    print("Mega Prime")
else:
    print("Not Mega Prime")