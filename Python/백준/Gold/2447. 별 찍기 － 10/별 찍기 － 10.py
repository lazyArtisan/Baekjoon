import sys
print = sys.stdout.write
N=int(input())
for i in range(N):
    for j in range(N):
        temp_i, temp_j = i, j
        flag = False
        if temp_i % 3 == 1 and temp_j % 3 == 1:
            flag = True
        else:
            while temp_i >= 3 and temp_j >= 3:
                temp_i //= 3
                temp_j //= 3
            
                if temp_i % 3 == 1 and temp_j % 3 == 1:
                    flag = True
                    break

        if flag:
            print(" ")
        else:
            print("*")
    print("\n")