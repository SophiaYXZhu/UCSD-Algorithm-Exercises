import sys

class StackWithMax():
    def __init__(self):
        self.__auxiliary_stack = []

    def Push(self, a):
        if len(self.__auxiliary_stack) == 0 or a > self.__auxiliary_stack[-1]:
            self.__auxiliary_stack.append(a)
        else:
            self.__auxiliary_stack.append(self.__auxiliary_stack[-1])

    def Pop(self):
        assert(len(self.__auxiliary_stack))
        self.__auxiliary_stack.pop()

    def Max(self):
        assert(len(self.__auxiliary_stack))
        return self.__auxiliary_stack[-1]

if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()
        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)