N=int(input())
stack=[]
for i in range(2,N+1):
    while N%i == 0:
        N=N//i
        stack.append(i)
    if N==1:
        break
for s in stack:
    print(s)
if N!=1 and not stack:
    print(N)