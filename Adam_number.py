def reverse(n):
    rev=0
    while n:
        r=n%10
        rev =rev*10+r
        n=n//10
    return rev
n=int(input())
temp=n
p=temp*temp
q=reverse(temp)
r=q*q
s=reverse(r)
if s==p:
    print("True")
else:
    print("False")