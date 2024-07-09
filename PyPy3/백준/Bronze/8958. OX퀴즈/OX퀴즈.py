N=int(input())
for _ in range(N):
    S=input()
    score=0
    streak=1
    for i in range(len(S)):
        if(S[i]=='O'): 
            score+=streak
            streak+=1
        else:
            streak=1
    print(score)