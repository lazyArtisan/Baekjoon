# 코인 금액 비싼것부터 최대한 넣어보기

import sys
input = sys.stdin.readline
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
cnt = 0

for coin in reversed(coins):
    while K - coin >= 0:
        K -= coin
        cnt += 1

print(cnt)