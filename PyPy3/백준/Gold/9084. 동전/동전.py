T = int(input())
for i in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    case_list = [0]*(M+1)
    case_list[0] = 1
    for coin in coins:
        for money in range(coin, M+1):
            case_list[money] += case_list[money-coin]
    print(case_list[M])