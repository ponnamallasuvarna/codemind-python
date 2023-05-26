import math
def isprime(n):
    if n==1:
        return False
    sq=int(math.sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
n=int(input())
t=n
rev=0
while n:
    r=n%10
    rev=rev*10+r
    n=n//10
p=rev
if isprime(t)and isprime(p):
    print("circular prime")
elif isprime(t):
    print("prime but not a circular prime")
else:
    print("not prime")
        