from __future__ import annotations
from typing import Any, Type
import sys
sys.setrecursionlimit(10**5)

class Node:
    def __init__(self, value, left: Node = None, right: Node = None):
        self.value = value
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def add_node(self, value):
        # 루트에 노드가 없으면 루트 생성
        if self.root is None:
            self.root = Node(value)
            return

        # 루트에서부터 탐색 시작
        p = self.root
        
        # 현재 노드보다 값이 크면 왼쪽,
        # 값이 작으면 오른쪽으로 가기
        while True:
            # 넣을 값이 현재 노드 값보다 작으면
            if value < p.value:
                # 왼쪽 자식이 없으면 노드 추가
                if p.left == None:
                    p.left = Node(value)
                    break
                # 왼쪽 자식이 있으면 포인터 변경
                else:
                    p = p.left

            # 넣을 값이 현재 노드 값보다 크면
            elif value > p.value:
                # 오른쪽 자식이 없으면 노드 추가
                if p.right == None:
                    p.right = Node(value)
                    break
                # 오른쪽 자식이 있으면 포인터 변경
                else:
                    p = p.right
    
    def postorder(self, p):
        
        if p == None:
            return

        self.postorder(p.left)
        self.postorder(p.right)
        print(p.value)

bst = BST()

while True:
    try:
        bst.add_node(int(input()))
    except:
        break

bst.postorder(bst.root)