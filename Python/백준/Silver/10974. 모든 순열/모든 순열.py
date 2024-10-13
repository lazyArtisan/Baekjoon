def permu(current, used, path):
    if len(path) == N:
        print(' '.join(map(str, path)))
        return
    for i in range(N):
        if not used[i]:
            used[i] = True
            permu(current + 1, used, path + [L[i]])
            used[i] = False

N = int(input())
L = sorted([i for i in range(1, N+1)])  # 사전 순을 보장하기 위해 정렬
used = [False] * N
permu(0, used, [])
