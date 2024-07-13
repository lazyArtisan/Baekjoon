import sys
input = sys.stdin.readline

V, E = map(int, input().split())

Edges = []

for _ in range(E):
    A, B, C = map(int, input().split())
    Edges.append([A, B, C])

def third_val(e):
    return(e[2])

Edges.sort(key = third_val)

# 크루스칼 알고리즘
# 1. 간선 데이터를 비용에 따라 오름차순으로 정렬
# 2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
#   사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킴
#   사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않음
# 3. 모든 간선에 대해 2번의 과정을 반복

# 각 정점이 들어있는 유니온을 기록함
union = [i for i in range(V)]

def kruskal(edge):
    s = union[edge[0]-1]
    e = union[edge[1]-1]

    if s == e:
        return 0
    else:
        for i in range(V):
            if union[i] == s:
                union[i] = e
        return edge[2]

result = 0
for edge in Edges:
    result += kruskal(edge)
print(result)

