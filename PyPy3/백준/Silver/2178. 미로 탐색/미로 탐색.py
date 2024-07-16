import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [input().strip() for _ in range(N)]

from collections import deque

def bfs(node, end, visited, waiting):
    visited.add(node)
    waiting.append(node)
    while len(waiting) != 0:
        global cnt 
        qSize = len(waiting)
        cnt += 1

        for _ in range(qSize):
        # 큐에서 확인할 칸을 하나 꺼낸다
            node = waiting.popleft()
            # print(node)

            # 도착 지점이었다면 경로를 표시하고 다음으로 넘어간다
            if node == end:
                return cnt

            # 상하좌우 칸을 확인한다
            x, y = node[0], node[1]
            dx_list = [-1,1,0,0]
            dy_list = [0,0,-1,1]

            for i in range(4):
                dx, dy = dx_list[i], dy_list[i]
                # 상하좌우 중에 유효한 칸이 있으면 큐에 넣는다
                if 0 <= x+dx <= N-1 and 0 <= y+dy <= M-1:
                    next = (x+dx,y+dy)
                    if next not in visited:
                        if graph[x+dx][y+dy] == '1':
                            waiting.append((x+dx,y+dy))
                            visited.add((x+dx,y+dy))                   
    return cnt

visited = set()
waiting = deque()
cnt = 0

print(bfs((0,0), (N-1,M-1), visited, waiting))