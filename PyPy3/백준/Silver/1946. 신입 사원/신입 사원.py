# 1차 성적으로 sort 후에
# 왼쪽부터 하나씩 순회를 한다
# 지금까지의 2차 순위 중 최고와 비교하여 낮으면 탈락

import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    apply = []
    for _ in range(N):        
        newbie = list(map(int,input().split()))
        apply.append(newbie)
    apply.sort()
    best_2nd = len(apply)+1
    cnt = 0
    for newbie in apply:   
        if newbie[1] < best_2nd:
            best_2nd = newbie[1]
            cnt += 1
    print(cnt)