import sys
input = sys.stdin.readline

class Node():
    def __init__(self,s,p,n):
        self.string = s
        self.prev = p
        self.next = n

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

    def addLeft(self,s):
        new_node = Node(s,self.prev,self)
        if self.prev:
            self.prev.next = new_node
        self.prev = new_node

init_str = input().strip()
M = int(input())
prev = None
for s in init_str:
    node = Node(s, prev, None) # 새 노드 만들고
    if prev:
        prev.next = node # 이전 노드에 연결
    prev = node # 이전 노드를 이번 노드로 만들기

# 커서를 노드 왼쪽에 두기 위해 마지막 배열 추가.
endNode = Node(None,node,None)
node.next = endNode
node = endNode

# 커서는 노드의 왼쪽에 있는 것으로 간주
for _ in range(M):
    oper = input().strip()
    if oper[0] == 'P':
        p, alp = oper.split()
        node.addLeft(alp) # alp를 커서 왼쪽(현재 노드 왼쪽)에 추가함

    elif oper == 'L':
        # 커서를 왼쪽으로 한 칸 옮김
        if node.prev:
            node = node.prev

    elif oper == 'D':
        # 커서를 오른쪽으로 한 칸 옮김
        if node.next:
            node = node.next

    elif oper == 'B':
        # 커서 왼쪽에 있는 문자(현재 노드의 이전 노드)를 삭제함
        if node.prev:
            node.prev.delete()

while node.prev != None: # == 으로 적은 실수
    node = node.prev
while node.string != None:
    print(node.string, end='')
    node = node.next

# 문자열을 노드로 만드는게 가장 이상적으로 보이긴 한데
# 실제로는 어떻게 구현하는 거지 그러면

