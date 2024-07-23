import sys, re
input = sys.stdin.readline

ex = input().strip()

# 첫 번째 '-'를 기준으로 문자열을 나누기
parts = ex.split('-')

# 첫 번째 부분은 '+'로 구분된 숫자들을 모두 더하기
first_part = sum(map(int, parts[0].split('+')))

# 나머지 부분들은 '-'가 있든 없든 모든 숫자들을 더한 후 빼기
remaining_parts = sum(sum(map(int, part.split('+'))) for part in parts[1:])

# 결과 계산
result = first_part - remaining_parts

print(result)