n = int(input())

# 동적 프로그래밍
# 하향식 접근법 사용해보기
# n이 될때까지 이전 결과 합하기 

def pibo(fn_1, fn, cnt):
    global n
    if cnt <= n:
        result = pibo(fn,fn_1+fn,cnt+1)
    else:
        return fn
    return result

if n==1:
    print(1)
elif n==2:
    print(1)
else:    
    print(pibo(1,1,3))