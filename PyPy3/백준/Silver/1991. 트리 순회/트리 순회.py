import sys
input = sys.stdin.readline

N = int(input())
# 딕셔너리로 트리 구현
tree = {}
for i in range(N):
    root, left, right = map(str, input().split())
    tree[root] = left, right
        
# 전위 순회
def preorder(v):
    if v != ".": # 루트 노드가 .이 아니면
        print(v, end="")
        preorder(tree[v][0]) # 왼쪽 노드 탐색
        preorder(tree[v][1]) # 오른쪽 노드 탐색

# 중위 순회
def inorder(v):
    if v != ".":
        inorder(tree[v][0])
        print(v, end="")
        inorder(tree[v][1])

# 후위 순회
def postorder(v):
    if v != ".":
        postorder(tree[v][0])
        postorder(tree[v][1])
        print(v, end="")
    
preorder('A')
print("")
inorder('A')
print("")
postorder('A')
