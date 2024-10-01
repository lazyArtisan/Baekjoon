def check_hand(hold_counts, found_head, memo):
    if sum(hold_counts) == 0:
        return True
    key = (hold_counts, found_head)
    if key in memo:
        return memo[key]
    for i in range(9):
        # 같은 패 3개로 몸통 만들기
        if hold_counts[i] >= 3:
            new_hold = list(hold_counts)
            new_hold[i] -= 3
            if check_hand(tuple(new_hold), found_head, memo):
                memo[key] = True
                return True
        # 연속 패 3개로 몸통 만들기
        if i <= 6 and hold_counts[i] > 0 and hold_counts[i+1] > 0 and hold_counts[i+2] > 0:
            new_hold = list(hold_counts)
            new_hold[i] -= 1
            new_hold[i+1] -= 1
            new_hold[i+2] -= 1
            if check_hand(tuple(new_hold), found_head, memo):
                memo[key] = True
                return True
        # 같은 패 2개로 머리 만들기
        if hold_counts[i] >=2 and not found_head:
            new_hold = list(hold_counts)
            new_hold[i] -=2
            if check_hand(tuple(new_hold), True, memo):
                memo[key] = True
                return True
    memo[key] = False
    return False

def check_ready(holding_counts, result, w):
    holding_counts = list(holding_counts)
    holding_counts[w-1] +=1
    # 머리 7개 체크
    seven_pairs = True
    for count in holding_counts:
        if count != 0 and count != 2:
            seven_pairs = False
            break
    if seven_pairs:
        result.add(w)
    else:
        memo = {}
        if check_hand(tuple(holding_counts), False, memo):
            result.add(w)
    holding_counts[w-1] -=1

# 입력 및 초기화
holding_counts = [0]*9
waiting_counts = [4]*9
temp = list(map(int,input().split()))
for t in temp:
    holding_counts[t-1] +=1
    waiting_counts[t-1] -=1
result = set()
for w in range(1,10):
    if waiting_counts[w-1] >0:
        check_ready(tuple(holding_counts), result, w)
if result:
    print(' '.join(map(str, sorted(result))))
else:
    print(-1)
