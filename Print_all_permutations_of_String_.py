from itertools import permutations
n=(input())
l=list(n)
prem=permutations(l)
for i in(prem):
    print("".join(i))