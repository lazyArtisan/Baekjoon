n=int(input())
ls=[list(map(int,input().split())) for _ in range(n)]

def iterative_dfs(x, y, visited, grid, threshold):
    stack = [(x, y)]
    n = len(grid)
    
    while stack:
        cx, cy = stack.pop()
        if cx < 0 or cy < 0 or cx >= n or cy >= n or grid[cx][cy] <= threshold or visited[cx][cy]:
            continue
        
        visited[cx][cy] = True
        
        # 상하좌우 방향으로 이동
        stack.append((cx + 1, cy))
        stack.append((cx - 1, cy))
        stack.append((cx, cy + 1))
        stack.append((cx, cy - 1))

def max_connected_areas(grid):
    n = len(grid)
    min_value = min(map(min, grid))
    max_value = max(map(max, grid))
    
    max_area_count = 0
    
    for threshold in range(min_value-1, max_value + 1):
        visited = [[False] * n for _ in range(n)]
        current_area_count = 0
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] > threshold and not visited[i][j]:
                    iterative_dfs(i, j, visited, grid, threshold)
                    current_area_count += 1
        
        max_area_count = max(max_area_count, current_area_count)
    
    return max_area_count

print(max_connected_areas(ls))