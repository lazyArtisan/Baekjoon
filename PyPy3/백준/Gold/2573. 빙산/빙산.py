import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

class Node:
    def __init__(self, i, j, height):
        self.locate = (i,j)
        self.height = height
        self.near = set()

N, M = map(int, input().split())
Arctic = []
Icebergs = set()

# 북극 상황 받아오기
for _ in range(N):
    field = list(map(int,input().split()))
    Arctic.append(field)

# 노드 만들기
for i in range(N):
    for j in range(M):
        height = Arctic[i][j]
        if height != 0:
            # 빙산 높이 대신 노드 넣고 빙산 명단 만들기
            Arctic[i][j] = Node(i,j,height)
            Icebergs.add(Arctic[i][j])

# 인접 노드 연결해주기
for iceberg in Icebergs:
    i, j = iceberg.locate[0], iceberg.locate[1]

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for k in range(4):
        near_iceberg = Arctic[i+dx[k]][j+dy[k]]
        if near_iceberg != 0:
            iceberg.near.add(near_iceberg)

# 빙하 녹이기    
def melting():
    # 높이를 낮추고
    for iceberg in Icebergs:
        if iceberg != 0:
            melt_h = 4 - len(iceberg.near)
            iceberg.height -= melt_h
    # 0 이하로 낮아지면 Arctic, near들의 near에서 삭제
    deleteQ = []
    for iceberg in Icebergs:
        if iceberg.height <= 0:
            for n in iceberg.near:
                n.near.remove(iceberg)
            i, j = iceberg.locate[0], iceberg.locate[1]
            Arctic[i][j] = 0
            deleteQ.append(iceberg)
    # Icebergs에서 삭제
    for d in deleteQ:
        Icebergs.remove(d)
 
# dfs
def dfs(ice, visited):
    global cnt
    visited.add(ice)
    cnt += 1
    if (len(ice.near) == 0):
        return
    for near in ice.near:
        if near not in visited:
            dfs(near, visited)

year = 0
while True:
    melting()
    year += 1
    cnt = 0
    # 끝까지 다 녹았는가?
    if len(Icebergs) == 0:
        year = 0
        break
    else:
        dfs(next(iter(Icebergs)),set())
        # 두 덩이로 나눠졌는가?
        if len(Icebergs) != cnt:
            break
    
print(year)


    