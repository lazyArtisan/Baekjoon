import copy
import sys
sys.setrecursionlimit(10**4)

R, C = map(int, input().split())

# 문자열 뜯어서 받기 힘들다
twMap = [[0 for _ in range(C)] for _ in range(R)]
Sx, Sy = 0, 0
for i in range(R):
    temp = input()
    for j in range(C):
        twMap[i][j] = temp[j]
for i in range(R):
    for j in range(C):
        if twMap[i][j] == 'S':
            Sx, Sy = i,j

# 고슴도치 퍼뜨리고
# 홍수 퍼뜨리기

arrived = False
cnt = 0

dx, dy = [1,-1,0,0], [0,0,1,-1]

while(1):
    # 고슴도치 움직임
    moved = False
    for i in range(R):
        for j in range(C):
            if twMap[i][j] == 'S':
                for k in range(4):
                    if (0<=i+dx[k]<R)and(0<=j+dy[k]<C):
                        if twMap[i+dx[k]][j+dy[k]] == '.':
                            twMap[i+dx[k]][j+dy[k]] = -2
                            moved = True
                        elif twMap[i+dx[k]][j+dy[k]] == 'D':
                            arrived = True    
    for i in range(R):
        for j in range(C):
            if twMap[i][j] == -2:
                twMap[i][j] = 'S'

    # 티떱숲 홍수 갱신 (중복 계산 조심)
    for i in range(R):
        for j in range(C):
            if twMap[i][j] == '*':
                for k in range(4):
                    if (0<=i+dx[k]<R)and(0<=j+dy[k]<C):
                        if(twMap[i+dx[k]][j+dy[k]] == '.' or twMap[i+dx[k]][j+dy[k]] == 'S'):
                            twMap[i+dx[k]][j+dy[k]] = -1    
    for i in range(R):
        for j in range(C):
            if twMap[i][j] == -1:
                twMap[i][j] = '*'
    cnt += 1 

    if arrived:
        break
    elif not moved:
        arrived = False
        break

if arrived:
    print(cnt)
else:
    print('KAKTUS')