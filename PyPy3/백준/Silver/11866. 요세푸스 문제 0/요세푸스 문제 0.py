N, K = map(int, input().split())
S = [i for i in range(1,N+1)]
A = []

idx = 0
for j in range(N):
    idx += K - 1
    idx = idx % N
    A.append(S[idx])
    del S[idx]
    N-=1

print('<' + ', '.join(map(str, A)) + '>')