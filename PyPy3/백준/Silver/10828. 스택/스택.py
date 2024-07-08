import sys
input = sys.stdin.readline

N = int(input())
S = []
for _ in range(N):
    command = input().split()
    if command[0] == "push":
        S.append(command[1])
    elif command[0] == "top":
        if len(S) == 0:
            print(-1)
        else:
            print(S[-1])
    elif command[0] == "size":
        print(len(S))
    elif command[0] == "empty":
        if(len(S)==0):
            print(1)
        else:
            print(0)
    elif command[0] == "pop":
        if len(S)==0:
            print(-1)
        else:
            print(S[-1])
            del S[-1]