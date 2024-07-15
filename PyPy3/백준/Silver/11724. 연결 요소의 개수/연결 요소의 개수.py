import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    visited.add(node)
    # print(node, end=' ')
    for near in graph[node]:
        if near not in visited:
            dfs(near)

visited = set()
result = 0

for i in range(1,N+1):
    if i not in visited:
        dfs(i)
        result += 1

print(result)