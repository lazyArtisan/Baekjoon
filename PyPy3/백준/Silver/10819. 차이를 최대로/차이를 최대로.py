import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
R_max = 0

def arrMax(A, B):
    global R_max
    if len(B) == N:
        R = 0
        for i in range(N - 1):
            R += abs(B[i] - B[i + 1])
        R_max = max(R, R_max)
        return

    for j in range(len(A)):
        B.append(A[j])
        arrMax(A[:j] + A[j+1:], B)
        B.pop()

arrMax(A, [])
print(R_max)