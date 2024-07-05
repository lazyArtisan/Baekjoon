import sys
from collections import defaultdict

N = int(sys.stdin.readline().strip())
S = {sys.stdin.readline().strip() for _ in range(N)}
D = defaultdict(list)

L = sorted(S)
L.sort()
N = len(L)

for i, string in enumerate(L):
  D[len(string)].append(string)

for key in sorted(D.keys()):
    for string in D[key]:
        print(string)