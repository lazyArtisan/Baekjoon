import sys
N = int(sys.stdin.readline())

L = [int(sys.stdin.readline().strip()) for _ in range(N)]

L.sort()

for i in range(N):
  print(L[i])