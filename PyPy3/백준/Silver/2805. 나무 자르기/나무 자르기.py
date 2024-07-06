import sys

S = list(map(int, sys.stdin.readline().strip().split()))
N = int(S[0]) # 나무의 수
M = int(S[1]) # 필요한 나무의 길이
T = list(map(int, sys.stdin.readline().strip().split())) # 나무들의 높이

# h만큼 벌목기 올렸을 때 얻는 나무의 양
def getTree(h):
  sum = 0
  for tree in T:
    if tree - h > 0:
      sum += tree - h
  return sum

start = 0
end = max(T)
mid = (start + end)//2

while start <= end:
  mid = (start+end)//2
  Get = getTree(mid)

  if Get == M:
    break
  elif Get <= M:
    end = mid - 1
    mid = (start+end)//2
  else:
    start = mid + 1
    mid = (start+end)//2

print(mid)