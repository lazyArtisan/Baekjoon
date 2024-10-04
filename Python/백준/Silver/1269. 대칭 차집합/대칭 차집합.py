# 대칭 차집합 : 두 집합의 합집합 중 교집합을 제거한다
a,b=map(int,input().split())
# A=list(map(int,input().split()))
# B=list(map(int,input().split()))
A=set(map(int,input().split()))
B=list(map(int,input().split()))
cnt=0
for e in B:
    if e in A:
        cnt+=1
    else:
        A.add(e)
print(len(A)-cnt)