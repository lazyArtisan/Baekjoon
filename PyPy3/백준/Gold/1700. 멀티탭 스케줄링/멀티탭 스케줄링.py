from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
L = list(map(int, input().split()))
# 삭제 연산 비싸지 않은 큐를 사용
order = defaultdict(deque)
for i in range(len(L)):
    order[L[i]].append(i)

cnt = 0
box = set()
# 다음에 가장 늦게 나올 물건을 먼저 뽑아버린다
for j in range(max(N,K)):
    # 현재 들어갈 물건의 현재 order 제거
    order[L[j]].popleft()
    if len(box) < N:
        # 현재 들어가 있는 물건 수보다 박스 크기가 더 크다면
        box.add(L[j])
    else:
        if L[j] in box:
            # 현재 들어갈 물건이 박스에 이미 있다면 스킵
            continue
        else:
            # 다음에 가장 늦게 나올 물건 고르기
            latest_order, latest_obj = 0, 0
            for obj in box:    
                # 앞으로 안 나올거면 빼버려도 상관 없음
                if not order[obj]:
                    latest_obj = obj
                    break        
                elif latest_order < order[obj][0]:
                    latest_order = order[obj][0]
                    latest_obj = obj
            box.remove(latest_obj)
            box.add(L[j])
            cnt += 1

print(cnt)
