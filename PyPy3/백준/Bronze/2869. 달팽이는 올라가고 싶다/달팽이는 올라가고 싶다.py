import math
A, B, V = map(int, input().split())
print(math.ceil(1+(V-A)/(A-B)))

# 마지막날 제외하곤 A-B만큼 올라간다
# (A-B)*(D-1) + A > V
# (A-B)*(D-1) > V-A
# D-1 > (V-A)/(A-B)
# D > 1+(V-A)/(A-B)