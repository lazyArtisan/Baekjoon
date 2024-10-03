import sys
input=sys.stdin.readline
n=int(input())
word=input()
res=0
temp=''
cnt=0
for i in range(n):
    #정수로변환했더니1에서9사이였다면문자열더하기
    #문자열더하다가자리수7이상이면히든넘버가아님
    #문자열더하다가문자가나오면히든넘버가아님
    if '0'<=word[i]<='9':
        temp+=word[i]
        cnt+=1
        if cnt>=7:
            temp=''
    elif temp:
        res+=int(temp)
        temp=''
        cnt=0
if temp:
    res+=int(temp)
print(res)