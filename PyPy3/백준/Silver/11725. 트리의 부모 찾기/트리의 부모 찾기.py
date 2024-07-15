import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    global result
    visited.add(node)
    # print(node, end=' ')
    for near in graph[node]:
        if near not in visited:
            parents[near]=node
            dfs(near)

visited = set()
parents = [i for i in range(N+1)]
result = 0

dfs(1)

for i in range(2,N+1):
    print(parents[i])