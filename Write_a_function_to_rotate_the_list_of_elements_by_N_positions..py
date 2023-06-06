def rotate(li,n):
    for i in range(n):
        li.insert(0,li.pop())
    return li
m=int(input())
li=list(map(int,input().split()))
k=int(input())
print(*(rotate(li,k)))
