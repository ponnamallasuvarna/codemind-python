n=int(input())
n1=0
n2=1
c=2
print(n1,end=" ")
print(n2,end=" ")
while c<n:
    n3=n1+n2
    print(n3,end=" ")
    c=c+1
    n1=n2
    n2=n3