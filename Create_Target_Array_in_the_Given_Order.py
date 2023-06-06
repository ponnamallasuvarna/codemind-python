n=int(input())
l=list(map(int,input().split()))
m=int(input())
k=list(map(int,input().split()))
m=[]
i=0
j=0
while i!=len(l)and j!=len(k):
    m.insert(k[j],l[i])
    i=i+1
    j+=1
print(*m)