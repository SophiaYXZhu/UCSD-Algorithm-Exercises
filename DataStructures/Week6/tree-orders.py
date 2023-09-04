import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c
    self.inorder_result = []
    self.preorder_result = []
    self.postorder_result = []

  def inOrder(self, root):
    if root != -1:
      self.inOrder(self.left[root])
      self.inorder_result.append(self.key[root])
      self.inOrder(self.right[root])
    return self.inorder_result

  def preOrder(self, root):
    if root != -1:
      self.preorder_result.append(self.key[root])
      self.preOrder(self.left[root])
      self.preOrder(self.right[root])
    return self.preorder_result

  def postOrder(self, root):
    if root != -1:
      self.postOrder(self.left[root])
      self.postOrder(self.right[root])
      self.postorder_result.append(self.key[root])
    return self.postorder_result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder(0)))
	print(" ".join(str(x) for x in tree.preOrder(0)))
	print(" ".join(str(x) for x in tree.postOrder(0)))

threading.Thread(target=main).start()
