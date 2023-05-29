n=input()
v=0
c=0
p=0
o=0
for i in n:
    if i.isdigit():
        p=p+1
    elif i.isalpha():
        v=v+1
    elif i==" ":
        o=o+1
    else:
        c=c+1
print(c)