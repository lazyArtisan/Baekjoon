import math

N = int(input())
nums = input().split()
count = 0

for i in range(N):
    num = int(nums[i])
    
    if num == 1:
        continue
    
    isP = True    
    for j in range(2, int(math.sqrt(num))+1):
        if num % j == 0:
            isP = False
            break
            
    if isP == True:
        count+=1
        
print(count)
    