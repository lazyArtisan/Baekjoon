import sys

S = [int(sys.stdin.readline().strip()) for _ in range(9)]
count = 0

fraud_sum = sum(S) - 100

for i in range(9):
  fraud_a = S[i]
  fraud_b = fraud_sum - fraud_a
  if fraud_b in S and fraud_a != fraud_b:
    S.remove(fraud_a)
    S.remove(fraud_b)
    break

S.sort()

for i in S:
  print(i)