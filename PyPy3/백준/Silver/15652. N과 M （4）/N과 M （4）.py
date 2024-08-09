N, M = map(int, input().split())

def combi(l,arr):
    global N, M

    if l != 0 and l != 1 and arr[-2] > arr[-1]:
        return

    if l >= M:
        for n in arr:
            print(n,end=' ')
        print()
        return

    for i in range(1,N+1):
        combi(l+1,arr+[i])

combi(0,[])