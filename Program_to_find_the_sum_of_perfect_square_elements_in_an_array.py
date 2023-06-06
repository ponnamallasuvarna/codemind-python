import math 
def perfect(n):
    p=int(math.sqrt(n))
    if p*p==n:
        return True
    else:
        return False
n=int(input())
lst=list(map(int,input().split()))
s=0
for i in lst:
    if perfect(i):
        s+=i
print(s)
    