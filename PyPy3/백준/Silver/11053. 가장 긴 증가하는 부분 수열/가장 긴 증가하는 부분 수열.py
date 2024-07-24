# 인덱스를 매번 이전과 비교하여 각각 큰지 아닌지, 작아야 +1
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
dp = [1]*N

for i in range(1,N):
    for j in range(i):
        if A[j] < A[i] and dp[j]+1 >= dp[i]:
            dp[i] = dp[j]+1
print(max(dp))