result = 0

def dfs(node, visited):
    global result
    visited.append(node)
    if len(graph[node]) == 0:
        return
    for near in graph[node]:
        if near not in visited:
            if A[near-1]=='1':
                result += 1
            else:
                dfs(near, visited)

N = int(input())
A = input()

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,N+1):
    # 실내인 점을 찾았다면
    if A[i-1] == '1':
        dfs(int(i), [])

print(result)
