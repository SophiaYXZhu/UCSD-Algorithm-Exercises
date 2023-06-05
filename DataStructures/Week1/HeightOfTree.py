import sys, threading
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)

class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.nodes = [[] for i in range(self.n)]
        self.root = None
        for child_idx in range(self.n):
            parent_idx = self.parent[child_idx]
            if parent_idx == -1:
                self.root = child_idx
            else:
                self.nodes[parent_idx].append(child_idx)

    def compute_height(self):
        maxHeight = 0
        for vertex in range(self.n):
                height = 0
                i = vertex
                while i != -1:
                    height += 1
                    i = self.parent[i]
                maxHeight = max(maxHeight, height)
        return maxHeight
    
    def find_height(self, node_idx):
        if self.nodes[node_idx] == 0:
            return 0
        value = [0]
        for i in range(len(self.nodes[node_idx])):
            value.append(self.find_height(self.nodes[node_idx][i]))
        return 1+max(value)

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.find_height(tree.root))
threading.Thread(target=main).start()