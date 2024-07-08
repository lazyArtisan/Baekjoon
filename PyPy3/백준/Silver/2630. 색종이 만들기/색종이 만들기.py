import sys
input = sys.stdin.readline

N = int(input())
P = [list(map(int, input().strip().split())) for _ in range(N)]

# def 색종이함수
# 종이의 길이가 1이라면 sum에 1을 더하고 return
# 전체 종이를 순회하며 같은 색인지 확인한다 (색이 달라지는지 확인한다)
# 전체 종이가 같다면
#   sum에 1을 더하고 return
# 전체 종이가 같은 색이 아니라면
#   1/4, 2/4, 3/4, 4/4 영역을 훑는다


def color_paper(x_s, x_e, y_s, y_e):
    global blue, white

    # 종이가 전부 같은 색깔인지 판별
    all_same = True
    color = P[x_s][y_s]
    # 범위를 훑으며 첫번째 셀과 같은 색깔인지 확인
    for x in range(x_s, x_e):
        # 모두 같지 않았다면 for문 취소
        if not all_same: break

        for y in range(y_s, y_e):
            if color != P[x][y]:
                all_same = False
                break
                    
    # 종이가 전부 파란색이었다면
    if all_same:
        if color == 1:
            blue += 1
            return
        else:
            white += 1
            return
    # 하나라도 다른 색깔이 있었다면
    else:
        x_mid = (x_s+x_e)//2
        y_mid = (y_s+y_e)//2
        color_paper(x_s, x_mid, y_s, y_mid) # 1/4
        color_paper(x_mid, x_e, y_s, y_mid) # 2/4
        color_paper(x_s, x_mid, y_mid, y_e) # 3/4
        color_paper(x_mid, x_e, y_mid, y_e) # 4/4

white = 0
blue = 0
color_paper(0, N, 0, N)

print(white)
print(blue)