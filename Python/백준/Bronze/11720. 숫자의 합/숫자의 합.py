import sys
input=sys.stdin.readline
N=int(input())
K=input().strip()
s=0
for n in K:
    s+=int(n)
print(s)