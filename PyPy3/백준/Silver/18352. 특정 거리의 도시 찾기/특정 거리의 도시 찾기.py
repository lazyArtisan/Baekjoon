import sys
input = sys.stdin.readline

# bfs 한 뒤에 depth가 k인 도시들을 출력한다
# visited 필요 없을듯?
# 최솟값을 담는 배열을 하나 만들면 될듯

N, M, K, X = map(int, input().split())

# graph = {i: [] for i in range(1,N+1)}
graph = [[] for i in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

from collections import deque

def bfs(node, waiting):
    visited = [-1]*(N+1)
    waiting.append(node)
    visited[node] = 0
    depth = 0

    while len(waiting) != 0:
        qSize = len(waiting)
        depth += 1

        for _ in range(qSize):
            node = waiting.popleft()
            for near in graph[node]:
                # 최단거리 갱신 및 조건 파악
                if visited[near] == -1:
                    waiting.append(near)
                    visited[near] = 0

        if depth == K:
            return waiting
        
    return waiting

waiting = deque()

courses = list(bfs(X, waiting))
if len(courses) == 0:
    print(-1)
else:
    courses.sort()
    for course in courses:
        print(course)

# '최단 거리'가 정확히 K인 모든 도시들의 번호 출력
# 다익스트라로도, bfs로도 된다고 함

