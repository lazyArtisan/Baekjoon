from collections import deque
def bfs(stn):
    Q = deque()
    Q.append(stn)
    while Q:
        stn = Q.popleft()
        for next, time in graph[stn]:
            # 환승 정보 초기화
            new_trans=dp[stn][0]
            new_time=dp[stn][1]+time
            next_trans = dp[next][0]
            if cpn[stn] != cpn[next]:
                new_trans+=1
            # 환승 횟수가 적거나 같으면 갱신, 아니면 넘어가기
            if new_trans > next_trans or new_trans > dp[M][0]:
                continue
            elif new_trans < next_trans:
                dp[next] = [new_trans, new_time]
            else: # 환승 횟수가 같고 시간이 적으면
                if new_time < dp[next][1]:
                    dp[next][1] = new_time
                else:
                    continue
            # 도착한거 아니면 다음으로
            if next != M:
                Q.append(next)
            
N,M=map(int,input().split()) # N:지하철역 개수, M: 도착지 번호
cpn=[0]*N # 지하철역 운영 회사 정보 (역은 0부터 N-1까지)
graph=[[] for _ in range(N)]
dp=[[float('inf'),float('inf')] for _ in range(N)]
dp[0]=[0,0]
for i in range(N):
    cpn[i]=int(input())
for i in range(N):
    temp=list(map(int,input().split()))
    for stn, time in enumerate(temp):
        if time != 0:
            graph[i].append((stn,time))
bfs(0)
print(dp[M][0],dp[M][1]) # 환승 횟수, 소요 시간 출력