S = int(input())

for _ in range(S):
    r, s = input().split()
    r = int(r)
    s_new = ""
    for i in range(len(s)):
        s_new += s[i] * r
    print(s_new)