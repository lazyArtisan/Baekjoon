N=int(input())
num_card=list(map(int,input().split()))
M=int(input())
check_list=list(map(int,input().split()))
num_card.sort()
for check_num in check_list:
    find = 0
    s,e=0,len(num_card)-1
    while s<=e:
        mid = (s+e)//2
        if num_card[mid] > check_num:
            e = mid-1
        elif num_card[mid] < check_num:
            s = mid+1
        else:
            find = 1
            break
    print(find, end=' ')