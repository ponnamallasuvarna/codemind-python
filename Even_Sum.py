n=int(input())
li=list(map(int,input().split()))
even=[even for even in li if even%2==0 ]
print(sum(even))