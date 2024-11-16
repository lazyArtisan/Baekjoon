# 그냥 나눈 몫이 해당 랜선에서 얻을 수 있는 랜선 개수
# 가능한 최대 길이는 랜선의 최소값
# 거기서부터 0까지 이분탐색 조진 후에
# K개의 랜선을 탐색한 길이로 나누면 랜선 몇 개 가질 수 있는지
# 최소 길이보다 크더라도 그냥 못 만든다고 무시해버리고도 목표량 달성 가능할수도
K, N = map(int,input().split())
LAN = [int(input()) for _ in range(K)]
s, e = 1, max(LAN)
while (s<=e):
    sub_sum = 0
    mid = (s+e)//2
    for L in LAN:
        if L >= mid:
            sub_sum += L//mid
    if sub_sum >= N:
        s = mid + 1
    elif sub_sum < N:
        e = mid - 1
print((s+e)//2)