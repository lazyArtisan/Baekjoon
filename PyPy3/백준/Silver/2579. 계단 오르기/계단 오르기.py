# 1계단이나 2계단 오를 수 있음
# 3번 연속 1계단 오르면 안됨
# 마지막 도착 계단을 반드시 밟아야 함

# 배열에 현재 계단까지 얻은 최고 점수와 
# 1계단을 이전에 0번 뛰었는지 1번 뛰었는지 2번 뛰었는지 저장

# 각 계단에서 1계단 뛰거나 2계단 뛰기

import sys
input = sys.stdin.readline

N = int(input())
Stairs = [0]
# 각각의 계단에 대해 이전에 뛴 1계단 횟수마다 최고 점수 저장
Record = []
for i in range(N+1):
    Record.append([0,0])
for _ in range(N):
    Stairs.append(int(input()))

Record[1][0] = Stairs[1]
# 모든 계단에서 2갈래씩 앞으로
for i in range(N):
    if i+1 < len(Stairs):
        if Record[i+1][1] < Record[i][0]+Stairs[i+1]:
            Record[i+1][1] = Record[i][0]+Stairs[i+1]

    if i+2 < len(Stairs):
        for j in range(2):
            if Record[i+2][0] < Record[i][j]+Stairs[i+2]:
                Record[i+2][0] = Record[i][j]+Stairs[i+2]

print(max(Record[-1]))  