s=input()
l=list(s)
p="aeiou"
for i in range(0,len(l)):
    if l[i] in p:
        l[i]=1
    else:
        l[i]=0
for i in range(0,len(l)-1,1):
    if l[i]==l[i+1]:
        l[i+1]="*"
li=[]
for i in range(0,len(l)):
    if l[i]!="*":
        li.append(l[i])
for i in range(0,len(li)):
    if li[i]:
        li[i]="V"
    else:
        li[i]="C"
print("".join(li))