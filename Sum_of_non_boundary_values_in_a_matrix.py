r,c=map(int,input().split())
lst=[list(map(int,input().split()))for i in range(r)]
a=[]
b=[]
for i in range(1,len(lst)-1,1):
    a.append(lst[i])
for i in a:
    for j in range(1,len(i)-1,1):
        b.append(i[j])
print(sum(b))
    