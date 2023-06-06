n=int(input())
lst=list(map(int,input().split()))
a=[]
b=[]
for i in range(0,len(lst)//2):
    a.append(lst[i])
for i in range(len(lst)//2,len(lst)):
    b.append(lst[i])
b.reverse()
print(*(b+a))