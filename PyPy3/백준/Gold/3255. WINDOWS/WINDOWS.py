N=int(input())
clicked=set()
cnt_first=1
btn_graph=dict()
for _ in range(N):
    lur,luc,rdr,rdc = tuple(map(int,input().split()))
    if cnt_first==1:
        first_btn=(lur,rdc)
        cnt_first+=1
    for btn in btn_graph:
        btn_r,btn_c = btn
        if lur <= btn_r <= rdr and luc <= btn_c <= rdc:
            btn_graph[(btn_r,btn_c)].append((lur,rdc))
    btn_graph[(lur,rdc)] = []

stack=[]
stack.append(first_btn)
cnt=0
while stack:
    cnt+=1
    btn = stack.pop()
    for btn_needed in btn_graph[btn]:
        if btn_needed not in clicked:
            clicked.add(btn_needed)
            stack.append(btn_needed)
    
print(cnt)