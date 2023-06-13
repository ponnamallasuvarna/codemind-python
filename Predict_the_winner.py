n=int(input())
lst=list(map(int,input().split()))
s=0
k=0
for i in range(0,2):
    s+=lst[i]
for i in range(2,len(lst)):
    k+=lst[i]
p=abs(s-k)
if p%4==0:
    print("X")
else:
    print("Y")