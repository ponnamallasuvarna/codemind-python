n=int(input())
lst=list(map(int,input().split()))
for i in range(0,len(lst)-1):
    if lst[i]<lst[i+1]:
        print("no")
        break
else:
    print("yes")