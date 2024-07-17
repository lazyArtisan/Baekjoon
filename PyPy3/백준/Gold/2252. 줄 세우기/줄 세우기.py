import sys
input = sys.stdin.readline

N, M = map(int,input().split())

# 진입차수 관리하는 리스트
indegree = [0 for _ in range(N+1)]

# 딕셔너리로 인접 리스트 구현
order = dict()
for i in range(N+1):
    order[i] = set()

for j in range(M):
    A, B = map(int, input().split())
    order[A].add(B)
    indegree[B] += 1

# 위상 정렬 실행
# 진입하는 간선이 없는 노드를 큐에 담는다.
# 큐에서 노드를 꺼내고 노드에 연결된 간선을 없앤다.
# 1번과 2번을 반복한다.

# 진입 차수에 대한 정보가 필요
# 노드 큐 길이도 따로 관리하면 성능 약간 빨라질듯

from collections import deque

# 진입차수가 0이 된 노드들을 관리하는 큐
nodeQueue = deque()
for i in range(len(indegree)):
    if indegree[i] == 0:
        nodeQueue.append(i)

# 최종 순서를 담는 리스트
final_order = []

# 큐에서 노드를 꺼내고 연결된 간선을 없앤다
while nodeQueue:    
    node = nodeQueue.pop()
    final_order.append(node)
    for next in order[node]:
        indegree[next] -= 1
        if indegree[next] == 0:
            nodeQueue.append(next)
del final_order[-1]
for order in final_order:
    print(order, end=' ')
