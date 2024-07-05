
N = int(input()) # 사막 크기
S = input().split() # 사막
M = int(input()) # 바늘 개수
S_find = input().split() # 찾아야 하는 바늘들

S.sort()

for i in range(M):
  isIn = 0
  need = S_find[i]
  start = 0
  idx_half = N//2
  end = N-1

  # 이분 탐색
  while (start <= end):
    if S[idx_half] == need:
      isIn = 1
      break      
    elif S[idx_half] < need:
      start = idx_half + 1
      idx_half = (start+end)//2
    else:
      end = idx_half -1
      idx_half = (start+end)//2

  print(isIn)