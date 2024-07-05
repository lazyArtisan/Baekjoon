import sys

N = int(sys.stdin.readline().strip())
L = []
for i in range(N):
    L.append(int(sys.stdin.readline().strip()))
L.sort()

for i in range(N):
    print(L[i])