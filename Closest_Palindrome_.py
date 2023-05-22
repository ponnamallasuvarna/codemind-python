def isprime(n):
    n=n-1
    while n!=0:
        p=str(n)
        q=p[::-1]
        if p==q:
            return q
            break
        else:
            n=n-1
def isprima(n):
    n=n+1
    while n!=0:
        p=str(n)
        q=p[::-1]
        if p==q:
            return q
            break
        else:
            n=n+1
n=int(input())
a=isprime(n)
b=isprima(n)
if abs(n-int(a))<abs(n-int(b)):
    print(int(a))
elif abs(n-int(a))==abs(n-int(b)):
    print(int(a),int(b))
else:
    print(int(b))