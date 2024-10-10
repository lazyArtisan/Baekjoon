# 가장 쉬운 해결책 : 자연수 N부터 1씩 낮추면서 분해합과 같은지 확인해보기

N=int(input())
answer = 0
for i in range(N,-1,-1):
    num_sum = i
    temp = i
    while temp != 0:
        num_sum += temp % 10
        temp //= 10
    if num_sum == N:
        answer = i
print(answer)