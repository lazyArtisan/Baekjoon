N, M = map(int, input().split())

arr = [i for i in range(1,N+1)]

def permutation(arr, case):
    if len(arr) == N-M:
        for n in case:
            print(n, end=' ')
        print()
        return

    for i in range(len(arr)):
        case.append(arr[i])
        permutation(arr[:i]+arr[i+1:len(arr)],case)
        case.pop()

permutation(arr,[])