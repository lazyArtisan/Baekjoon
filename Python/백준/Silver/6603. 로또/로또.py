# 그냥 조합 문제 아님?
from itertools import combinations
while 1:
    tc = list(map(int,input().split()))
    if tc == [0]:
        break
    for combi in combinations(tc[1:], 6):
        for c in combi:
            print(c, end=' ')
        print('')
    print('')