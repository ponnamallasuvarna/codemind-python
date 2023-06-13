n=int(input())
li=list(map(int,input().split()))
s=[str(integer)for integer in li]
a_string="".join(s)
res=int(a_string)
m=res+1
l=[]
while m:
    r=m%10
    l.append(r)
    m=m//10
l.reverse()
print(*l)