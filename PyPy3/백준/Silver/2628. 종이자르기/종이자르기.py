W, H = map(int, input().split())
N = int(input())
arr_W, arr_H = [0], [0]
for i in range(N):
    WorH, line = map(int, input().split())
    if WorH == 1:
        arr_W.append(line)
    else:
        arr_H.append(line)

arr_W.append(W)
arr_H.append(H)

arr_W.sort()
arr_H.sort()

W_max, H_max = 0, 0
for i in range(len(arr_W)-1):
    W_max = max(W_max,arr_W[i+1]-arr_W[i]) 
for i in range(len(arr_H)-1):
    H_max = max(H_max,arr_H[i+1]-arr_H[i])

print(W_max * H_max)