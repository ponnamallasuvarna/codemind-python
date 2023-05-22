n=int(input())
t=str(n)
p=str(n*n)
if p.endswith(t):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")