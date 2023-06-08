n=int(input())
lst=list(map(int,input().split()))
s=0
p=0
for i in range(0,(n+2)//2):
    s+=i
for j in range(0,(n+1)):
    p+=j
print(s)
print(p-s)