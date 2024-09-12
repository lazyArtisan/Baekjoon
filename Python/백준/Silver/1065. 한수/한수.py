N=int(input())
cnt = 0
for i in range(1,N+1):
    num = i
    stack=[]
    while num > 0:
        stack.append(num%10)
        num = int(num/10)
    if len(stack) == 1:
        cnt+=1
        continue
    dv = stack[1] - stack[0]
    isHS = True
    while len(stack) > 1:
        last = stack.pop()
        blast = stack[-1]
        if (last - blast) != dv:
            isHS = False
            break
    if isHS:
        cnt+=1
print(cnt)