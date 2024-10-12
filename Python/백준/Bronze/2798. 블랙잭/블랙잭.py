N, M = map(int,input().split())
L = list(map(int,input().split()))
res=0
temp=0
for i in range(N):
    temp+=L[i]
    if temp > M:
        temp-=L[i]
        continue
    for j in range(i+1,N):
        temp+=L[j]
        if temp > M:
            temp-=L[j]
            continue
        for k in range(j+1,N):
            temp+=L[k]
            if M-temp >= 0 and M-res >= M-temp:
                res=temp
            temp-=L[k]
        temp-=L[j]
    temp-=L[i]
print(res)