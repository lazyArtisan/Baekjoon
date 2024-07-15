import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

from collections import deque

def bfs(node, visited, waiting):
    visited.append(node)
    waiting.append(node)
    color[node] = 1
    while len(waiting) != 0:
        node = waiting.popleft()
        for near in graph[node]:
            if near not in visited:
                waiting.append(near)
                visited.append(near)
            if color[near] is None:
                color[near] = color[node] * -1
            else:
                if color[near] == color[node]:
                    return False
    return True

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    color = [None for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a) 
    
    visited = []
    waiting = deque()
    bipartite = True

    for i in range(1,V+1):
        if i not in visited:
            if not bfs(i,visited, waiting):
                bipartite = False
                break
    if bipartite:
        print('YES')
    else:
        print('NO')
            