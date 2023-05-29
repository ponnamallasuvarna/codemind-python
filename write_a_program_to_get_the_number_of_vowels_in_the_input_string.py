s=input().lower()
p='aeiou'
c=0
for i in s:
    if i in p:
        c=c+1
print(c)