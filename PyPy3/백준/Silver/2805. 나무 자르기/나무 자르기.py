import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
pl, pr = 0, max(arr)
while(pl <= pr):
    res=0
    p = (pl+pr)//2
    for h in arr:
        if h-p > 0:
            res+=(h-p)
    if M > res:
        pr = p-1
    elif M < res:
        pl = p+1
    else:
        break
if M > res:
    print(p-1)
else:
    print(p)