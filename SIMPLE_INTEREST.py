def simpleinterest(x,y,z):
    s=(x*y*z)//100
    return s
P,T,R=map(int,input().split())
s=simpleinterest(P,T,R)
print(s)