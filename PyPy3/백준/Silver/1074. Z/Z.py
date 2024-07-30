# 사분면으로 쪼개기
N, r, c = map(int,input().split())
x, y, size = 0, 0, 2**N
cnt=0
def visitOrder(x,y,size):
    global cnt

    if(size == 1):
        print(int(cnt))
        return
    
    half = size/2

    if x+half > c:
        if y+half > r:
            return visitOrder(x,y,half)
        else:
            cnt+=size*size*(2/4)
            return visitOrder(x,y+half,half)
    else:
        if y+half > r:
            cnt+=size*size*(1/4)
            return visitOrder(x+half,y,half)
        else:
            cnt+=size*size*(3/4)
            return visitOrder(x+half,y+half,half)

visitOrder(x,y,size)