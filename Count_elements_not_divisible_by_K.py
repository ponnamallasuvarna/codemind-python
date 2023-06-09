a,b=map(int,input().split())
lst=list(map(int,input().split()))
ct=0
for i in lst:
    if i%b!=0:
        ct+=1
print(ct)