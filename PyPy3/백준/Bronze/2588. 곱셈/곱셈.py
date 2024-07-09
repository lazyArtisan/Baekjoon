F = int(input())
S = input()
S_L = list(S)

L = len(S_L)

for i in range(L):
    print(int(S_L[L-i-1])*F)
print(F * int(S))