R, C = map(int, input().split())
twMap = [list(input()) for _ in range(R)]
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