import sys
input = sys.stdin.readline

# N은 세로 길이, M은 가로 길이
N, M = map(int, input().split())
floor = []
visitied = []

for _ in range(N):
    floor.append(input().strip())

# 세로와 가로 길이 바꿈
floor_mirror = ['' for _ in range(M)]

# 행렬 90도 회전
for i in range(M-1,-1,-1):
    for j in range(N):
        floor_mirror[M-1-i] += floor[j][i]

cnt = 0

for i in range(N):
    onlyHorizon = floor[i].split('|')
    for horizon in onlyHorizon:
        if horizon:
            cnt += 1

for i in range(M):
    onlyVertical = floor_mirror[i].split('-')
    for vertical in onlyVertical:
        if vertical:
            cnt += 1

print(cnt)