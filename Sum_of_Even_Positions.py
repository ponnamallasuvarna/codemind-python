n=int(input())
li=list(map(int,input().split()))
i=[i for i in li[0::2]]
print(sum(i))