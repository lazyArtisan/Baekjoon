import sys
input = sys.stdin.read

data = input().split()
index = 0
T = int(data[index])
index += 1

results = []

for _ in range(T):
    N = int(data[index])
    index += 1
    apply = []
    for _ in range(N):        
        newbie = (int(data[index]), int(data[index + 1]))
        apply.append(newbie)
        index += 2
    
    apply.sort()
    best_2nd = float('inf')
    cnt = 0
    for newbie in apply:   
        if newbie[1] < best_2nd:
            best_2nd = newbie[1]
            cnt += 1
    
    results.append(cnt)

print("\n".join(map(str, results)))
