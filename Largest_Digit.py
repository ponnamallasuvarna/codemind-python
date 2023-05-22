n=int(input())
list=[]
while n!=0:
    r=n%10
    list.append(r)
    n=n//10
print(max(list))