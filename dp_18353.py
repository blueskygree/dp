import sys
input=sys.stdin.readline

n=int(input())
data=list(map(int,input().split()))

d=[1]*(n+1)

for i in range(n):
    for j in range(i): 
        if data[i]<data[j]:
            d[i]=max(d[i],d[j]+1)

print(len(data)-max(d))