import sys
input = sys.stdin.readline

# N = 물품의 수, K = 배낭 용량
N, K = map(int,input().split())
objs = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (K + 1)

# 물건을 하나씩 순회한다
for weight, value in objs:
    # 배낭 용량을 하나씩 줄인다 (역순으로 순회)
    for j in range(K, weight - 1, -1):
        dp[j] = max(dp[j], dp[j - weight] + value)

print(dp[K])