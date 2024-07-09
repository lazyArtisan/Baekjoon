A, B, C = map(int, input().split())

R = A % C

def remainder(A, B, C):
    R = A % C
    if B == 1:
        return R
    elif B % 2 == 0: # 지수가 짝수면
        R = remainder(R*R, B//2, C)
        return R
    else:
        R = remainder(R*R,B//2,C) * R
        return R

print(remainder(A,B,C)%C)