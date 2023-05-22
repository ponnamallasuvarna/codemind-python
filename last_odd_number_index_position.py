n=int(input())
li=list(map(int,input().split()))
for i in range(n-1,-1,-1):
    if li[i]%2!=0:
        print(i)
        break