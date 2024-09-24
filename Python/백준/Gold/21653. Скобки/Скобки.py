bracket=input()
n=len(bracket)
stack=[]
res=0
cnt=0
for i in range(n):
    cnt+=1
    if stack and stack[-1]=='(' and bracket[i]==')':
        stack.pop()
    else:
        stack.append(bracket[i])        
    if not stack:
        res+=cnt*(cnt-1)/2
        cnt=0
res+=n*(n+1)/2+(n+1)
print(int(res))