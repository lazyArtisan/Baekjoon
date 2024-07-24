N, K = map(int,input().split())
times = [[] for _ in range(K+1)]
elec = list(map(int,input().split()))
for i in range(K) :
    times[elec[i]].append(i+1)

using = []
cnt = 0
for i in elec :
    if i in using :
        times[i].pop(0)
        continue
    if len(using) < N :
        using.append(i)
        times[i].pop(0)
    else :
        target = 0
        cnt += 1
        for j in using :
            if len(times[j]) == 0 :
                using.remove(j)
                break
            target = max(times[j][0],target)
            if target == times[j][0] :
                del_item = j
        if len(using) == N :
            using.remove(del_item)
        using.append(i)
        times[i].pop(0)
print(cnt)