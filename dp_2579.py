import sys
input=sys.stdin.readline

n=int(input())
d=[0]*301

data=[0]*301
for i in range(n):
    data[i]=int(input())

d[0]=data[0]
d[1]=data[0]+data[1]
d[2]=max(data[0]+data[2],data[1]+data[2]) # d[2]=max(data[0]+data[2],d[1],data[1]+data[2]) 아닌 이유:

for i in range(3,n):
    d[i]=max(d[i-2]+data[i],data[i-1]+data[i]+d[i-3]) # d[i]를 밟고 있다는 가정이기 때문에 d[1]이 들어가면 연속 3개를 밟는것이다.

print(d[n-1])