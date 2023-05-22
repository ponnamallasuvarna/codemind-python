n=int(input())
li=list(map(int,input().split()))
l=sum(li)
m=sum(li)
n=l//m
if n in li:
    print("True")
else:
    print("False")