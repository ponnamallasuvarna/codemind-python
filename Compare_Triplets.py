t=list(map(int,input().split()))
n=list(map(int,input().split()))
i=0
j=0
l=[]
k=0
c=0
while i!=len(t) and j!=len(n):
    if t[i]>n[j]:
        c+=1
    if t[i]<n[j]:
        k+=1
    i+=1
    j+=1
print(c,k)