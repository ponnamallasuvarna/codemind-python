s=input()
p="aeiouAEIOU"
k=[]
for i in s:
    if i in p and i not in k:
        k.append(i)
print(*k)