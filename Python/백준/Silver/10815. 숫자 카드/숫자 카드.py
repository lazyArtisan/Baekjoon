N = int(input()) # 상근이가 갖고 있는 카드 수
Nums = set(map(int,input().split())) # 숫자 카드에 적혀있는 정수
M = int(input())
Query = list(map(int,input().split())) # 숫자인지 아닌지 확인해야 하는 숫자들

for q in Query:
    if q in Nums:
        print("1",end=" ")
    else:
        print("0",end=" ")