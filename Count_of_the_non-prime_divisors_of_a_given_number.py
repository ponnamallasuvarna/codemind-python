import math
def isprime(n):
    s=int(math.sqrt(n))
    if n<2:
        return False
    for i in range(2,s+1):
        if n%i==0:
            return False
    return True
n=int(input())
l=[]
k=[]
c=0
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
for i in l:
    if not isprime(i):
        k.append(i)
print(len(k))
