n=input().split()
lst=list(n)
a=lst[-1]
b=min(a)
if b in a and b.lower()in a:
    print(b.lower())
else:
    print(b)