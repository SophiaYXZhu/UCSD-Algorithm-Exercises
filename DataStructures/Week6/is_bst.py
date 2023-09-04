import sys, threading

sys.setrecursionlimit(10**8)  # max depth of recursion
threading.stack_size(2**30)   # new thread will get stack of such size

class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

def IsBinarySearchTree(index, tree, min_key=float('-inf'), max_key=float('inf')):
    if index == -1:
        return True
    node = tree[index]
    if not (min_key < node.key < max_key):
        return False
    left_is_bst = IsBinarySearchTree(node.left, tree, min_key, node.key)
    right_is_bst = IsBinarySearchTree(node.right, tree, node.key, max_key)
    return left_is_bst and right_is_bst

def main():
    nodes = int(input().strip())
    if nodes == 0:
        print("CORRECT")
    else:
        tree = []
        for _ in range(nodes):
            key, left, right = map(int, input().strip().split())
            tree.append(Node(key, left, right))

        if IsBinarySearchTree(0, tree):
            print("CORRECT")
        else:
            print("INCORRECT")

threading.Thread(target=main).start()