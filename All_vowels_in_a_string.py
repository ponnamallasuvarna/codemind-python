def count(s):
    a="aeiou"
    c=0
    p=set(s)
    for i in p:
        if i in a:
            c=c+1
    return c
n=input()
if count(n)==5:
    print("True")
else:
    print("False")