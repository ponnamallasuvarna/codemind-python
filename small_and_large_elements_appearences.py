n=input()
s=[]
for i in n:
    if i!=" ":
        s.append(i)
u=max(s)
v=min(s)
a=[]
print(v,s.count(v),u,s.count(u),end=" ")