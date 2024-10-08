import sys
input = sys.stdin.readline
string = input().strip()
explosion = input().strip()
stack = []
# string 훑으면서 stack에 하나씩 넣을때마다
# explosion과 일치하는지 확인해보고, 일치하면 다 꺼내기
# explosion 길이만큼 stack과 explosion 역순회
# 일치하면 explosion 길이만큼 pop, stack 다 봤으면 break
for s in string:
    stack.append(s)
    idx = len(stack)-1
    flag = True
    for i in range(len(explosion)-1,-1,-1):
        if idx < 0 or explosion[i] != stack[idx]:
            flag = False
            break
        idx -= 1
    if flag:
        for _ in range(len(explosion)):
            stack.pop()
if stack:
    for s in stack:
        print(s,end='')
else:
    print('FRULA')