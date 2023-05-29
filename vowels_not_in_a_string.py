n=input()
a="aeiou"
l=[]
for i in n:
    if i in a:
        l.append(i)
p=[]
for i in a:
    if i not in l:
        p.append(i)
c=0
for i in a:
    if i in l:
        c=c+1
if c==5:
    print("0")
else:
    print(*p)