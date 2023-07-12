s=input()
n=list(s)
for i in range(0,len(n)):
    if n.count(n[i])==1:
        print(i)
        break
else:
    print("-1")