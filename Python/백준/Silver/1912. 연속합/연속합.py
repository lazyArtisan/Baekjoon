n = int(input())
a = list(map(int,input().split()))
d = [0]
for i in a:
    if d[-1] > 0:d.append(i + d[-1])
    else: d.append(i)
print(max(d[1:]))