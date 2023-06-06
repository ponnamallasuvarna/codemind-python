def even(n):
    l=[]
    while n!=0:
        r=n%10
        l.append(r)
        n=n//10
    if len(l)%2==0:
        return True
    else:
        return False
t=int(input())
li=list(map(int,input().split()))
c=0
for i in li:
    if even(i)==True:
        c+=1
print(c)