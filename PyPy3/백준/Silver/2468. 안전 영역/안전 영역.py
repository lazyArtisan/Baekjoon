import sys
sys.setrecursionlimit(10**5)
N = int(input())
height = []
for i in range(N):
    height.append(list(map(int,input().split())))
paper = [[0 for _ in range(N)] for _ in range(N)]

# 안전 영역 찾으면 일단 cnt +1
# 그 후 죄다 내린 비에 해당하는 숫자로 칠해버림

def bfs(i,j,x):
    global N
    if 0<=i<N and 0<=j<N:
        if(height[i][j]>x and paper[i][j]!=x):
            paper[i][j]=x
            bfs(i-1,j,x)
            bfs(i+1,j,x)
            bfs(i,j-1,x)
            bfs(i,j+1,x)
    
last = 0
for i in range(N):
    for j in range(N):
        last = max(last,height[i][j])

result=0
for x in range(last+1):
    cnt=0
    for i in range(N):
        for j in range(N):
            if(height[i][j]>x and paper[i][j]!=x):
                cnt+=1
                bfs(i,j,x)
    result=max(cnt,result)

if result==0:
    result=1

print(result)

