N=int(input())
# 버튼을 가린다면 선행 버튼 정보를 해당 칸에 추가
# 창이 100개 뿐이니까 매번 순회해도 문제 x
# 버튼의 위치 : (왼위세, 우아가)
# 그래프를 만든 후에 탐색하며 삭제

# 창이 어떤 버튼을 가린다면,
# 해당 버튼에 지금 창의 버튼을 연결해준다.
clicked=set()
cnt_first=1
btn_graph=dict()
for _ in range(N):
    # (왼위세,왼위가,우아세,우아가)
    lur,luc,rdr,rdc = tuple(map(int,input().split()))
    # 첫 버튼 기억해두기
    if cnt_first==1:
        first_btn=(lur,rdc)
        cnt_first+=1
    # 버튼들 순회하며 가리는지 안 가리는지 확인
    for btn in btn_graph:
        btn_r,btn_c = btn
        if lur <= btn_r <= rdr and luc <= btn_c <= rdc:
            btn_graph[(btn_r,btn_c)].append((lur,rdc))
    btn_graph[(lur,rdc)] = []

# dfs로 순회하며 필요한 버튼들 다 눌러주기
stack=[]
stack.append(first_btn)
cnt=0
while stack:
    cnt+=1
    btn = stack.pop()
    # 클릭 안 했었다면 클릭 예약
    for btn_needed in btn_graph[btn]:
        if btn_needed not in clicked:
            clicked.add(btn_needed)
            stack.append(btn_needed)
    
print(cnt)