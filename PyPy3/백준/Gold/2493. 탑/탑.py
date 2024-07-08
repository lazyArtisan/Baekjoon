import sys
input = sys.stdin.readline

N = int(input())
Tower = list(map(int, input().split()))

valid_idx = [0]
print(0, end='')

for i in range(1, len(Tower)):
    h = Tower[i]
    zeroEnd = True
    # 유효한 타워 높이의 인덱스들이 담긴 배열을 아래로 내려가며 순회
    for j in range(len(valid_idx)-1,-1,-1):
        # 타워 높이가 송신지보다 낮으면
        if Tower[valid_idx[j]] < h:
            del valid_idx[-1]
            if j == 0:
                valid_idx.append(i)
                print('', 0, end='')
                break
        # 타워 높이가 송신지보다 높으면
        else:
            print('', valid_idx[j]+1, end='')
            valid_idx.append(i)
            break