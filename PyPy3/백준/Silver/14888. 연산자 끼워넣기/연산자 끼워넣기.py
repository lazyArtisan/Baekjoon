N = int(input())
L = list(map(int, input().split()))
ope_list = list(map(int, input().split()))
res_list = set()

def brute(res,remain,a,b,c,d):
    if remain != 0:
        if a > 0:
            brute(res+L[-remain],remain-1,a-1,b,c,d)
        if b > 0:
            brute(res-L[-remain],remain-1,a,b-1,c,d)
        if c > 0:
            brute(res*L[-remain],remain-1,a,b,c-1,d)
        if d > 0:
            brute(int(res/L[-remain]),remain-1,a,b,c,d-1)
    else:
        res_list.add(res)
        return

a = ope_list[0]
b = ope_list[1]
c = ope_list[2]
d = ope_list[3]
brute(L[0],N-1,a,b,c,d)

maxR = max(res_list)
minR = min(res_list)
print(maxR)
print(minR)