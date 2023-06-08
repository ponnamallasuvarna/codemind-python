n=int(input())
li=list(map(int,input().split()))
l=[]
for i in range(1,len(li),2):
    l.append(li[i])
for i in l:
    if i%2==0:
        print("False")
        break
else:
    print("True")
        