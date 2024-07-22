F = input()
S = input()
L = [[0]*(len(S)+1) for i in range(len(F)+1)]

for i in range(1,len(F)+1):
    for j in range(1,len(S)+1):
        if F[i-1] == S[j-1]:
            L[i][j] = L[i-1][j-1] + 1
        else:
            L[i][j] += max(L[i-1][j],L[i][j-1])

print(L[i][j])