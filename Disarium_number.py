n=int(input())
x=n
y=n
len=0
while x>0:
    x=x//10
    len=len+1
s=0
while y>0:
    r=y%10
    s=s+int(r**len)
    y=y//10
    len=len-1
if s==n:
    print("True")
else:
    print("False")