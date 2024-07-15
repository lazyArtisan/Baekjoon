import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    global result
    visited.add(node)
    # print(node, end=' ')
    for near in graph[node]:
        if near not in visited:
            result += 1
            dfs(near)

visited = set()
result = 0

dfs(1)

print(result)