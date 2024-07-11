N, S = map(int, input().split())
L = list(map(int, input().split()))

Ans = 0
lim = len(L)-1

# i는 현재 인덱스, 
# R은 남아있는 원소 개수
# save는 현재까지의 sum
def sumTest(i, R, sum):
    global Ans
    sum += L[i]
    
    if (sum == S):
        Ans+=1
    if (R==0 or i==lim):
        return
        
    for j in range(i+1,N):
        sumTest(j,R-1,sum)

for i in range(N):
    sumTest(i,len(L),0)

print(Ans)