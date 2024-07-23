import sys
input = sys.stdin.readline
N = int(input())
meets = [tuple(map(int,input().split())) for _ in range(N)]
meets.sort(key=lambda x: (x[1], x[0]))
end, cnt = -1, 0
for meet in meets:
    if end <= meet[0]:
        cnt += 1
        end = meet[1]
print(cnt)