# 머리 : 같은 패 2개
# 몸통 : 연속 패 or 같은 패 3개
# 패가 4개면 머리도 몸통도 될 수 없음
# 36개 패 중 14개 모아서 (머리 1개, 몸통 4개) or (머리 7개)로 만들어야 함
# (머리 7개) : 같은 종류 머리 2개 있으면 안됨

# 패 13개가 있을 때 적당히 패 1개를 더 가져와서 패 14개로 완성하려고 함.

# 패 13개가 있고 남은 23개 중 어떤 패를 한 개 가져왔을 때, 
# 그 패가 완성될 수 있다면 그 패는 "대기패"라고 함.
# 13개의 패가 있을 때 대기패를 찾기

def check_head_body(hold,result,idx,found_head):
    Sum=0
    for i in hold:
        Sum+=hold[i]
    if Sum == 0:
        return True

    made=False

    for i in range(idx,10):
        # 1개면 (연속 3개)의 일원이 될 수 있음
        if i<8 and hold[i]==1 and hold[i+1]>0 and hold[i+2]>0:
            hold[i],hold[i+1],hold[i+2]=hold[i]-1,hold[i+1]-1,hold[i+2]-1
            if check_head_body(hold,result,i+1,found_head): made=True
            hold[i],hold[i+1],hold[i+2]=hold[i]+1,hold[i+1]+1,hold[i+2]+1
        # 2개면 (연속 3개)x2 혹은 머리가 될 수 있음
        if hold[i]==2 and not found_head:
            hold[i]-=2
            if check_head_body(hold,result,i+1,True): made=True
            hold[i]+=2
        if i<8 and hold[i]==2 and hold[i+1]>1 and hold[i+2]>1:
            hold[i],hold[i+1],hold[i+2]=hold[i]-2,hold[i+1]-2,hold[i+2]-2
            if check_head_body(hold,result,i+1,found_head): made=True
            hold[i],hold[i+1],hold[i+2]=hold[i]+2,hold[i+1]+2,hold[i+2]+2
        # 3개면 (높이 3개) 혹은 (연속 3개)+(머리)가 될 수 있음
        if hold[i]==3:
            hold[i]-=3
            if check_head_body(hold,result,i+1,found_head): made=True
            hold[i]+=3
        if i<8 and hold[i]==3 and hold[i+1]>0 and hold[i+2]>0 and not found_head:
            hold[i],hold[i+1],hold[i+2]=hold[i]-3,hold[i+1]-1,hold[i+2]-1
            if check_head_body(hold,result,i+1,True): made=True
            hold[i],hold[i+1],hold[i+2]=hold[i]+3,hold[i+1]+1,hold[i+2]+1 
        # 4개면 (연속 3개)x2+(머리) 혹은 (연속 3개)+(높이 3개)가 될 수 있음
        if i<8 and hold[i]==4 and hold[i+1]>1 and hold[i+2]>1 and not found_head:
            hold[i],hold[i+1],hold[i+2]=hold[i]-4,hold[i+1]-2,hold[i+2]-2
            if check_head_body(hold,result,i+1,True): made=True
            hold[i],hold[i+1],hold[i+2]=hold[i]+4,hold[i+1]+2,hold[i+2]+2
        if i<8 and hold[i]==4 and hold[i+1]>0 and hold[i+2]>0:
            hold[i],hold[i+1],hold[i+2]=hold[i]-4,hold[i+1]-1,hold[i+2]-1
            if check_head_body(hold,result,i+1,found_head): made=True
            hold[i],hold[i+1],hold[i+2]=hold[i]+4,hold[i+1]+1,hold[i+2]+1
        

    return made
            
def check_ready(holding,result,w):
    holding[w]+=1
    # 머리 7개 체크
    seven_head = True
    for h in holding:
        if holding[h] != 0 and holding[h] != 2:
            seven_head = False
            break
    if seven_head:
        result.add(w)
    # 머리 1개, 몸통 4개 체크
    if check_head_body(holding,result,1,False):
        result.add(w)
    holding[w]-=1

# waiting에 남은 숫자 중 하나 가져와서 판별
holding={i:0 for i in range(1,10)}
waiting={i:4 for i in range(1,10)}
temp=list(map(int,input().split()))
for t in temp:
    holding[t]+=1
    waiting[t]-=1
result=set()
for w in waiting:
    if waiting[w]>0:
        check_ready(holding,result,w)
result=list(result)
result.sort()
if result:
    for r in result:
        print(r,end=' ')
else:
    print(-1)