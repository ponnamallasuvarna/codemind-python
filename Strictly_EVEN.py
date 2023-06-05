n=int(input())
lst=list(map(int,input().split()))
l=[]
a=0
for i in range(0,n,2):
    if lst[i]%2==0:
        continue
    print(False)
    break
else:
    print(True)