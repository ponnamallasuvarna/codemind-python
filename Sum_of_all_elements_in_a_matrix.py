r,c=map(int,input().split())
mat=[]
for i in range(r):
    lst=list(map(int,input().split()))
    mat.append(lst)
p=[]
for i in mat:
    p.append(sum(i))
print(sum(p))