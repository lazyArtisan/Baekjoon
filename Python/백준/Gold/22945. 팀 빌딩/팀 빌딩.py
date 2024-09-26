N=int(input())
stat=list(map(int,input().split()))
s,e=0,len(stat)-1
res=0
while(s<e):
    team_stat = (e-s-1)*min(stat[s],stat[e])
    res=max(res,team_stat)
    if (stat[s]<=stat[e]): s+=1
    else: e-=1
print(res)