# stack=[]
# stack.append('a')
# stack.append('b')
# stack.append('c')
# stack.append(1)
# stack.append(2)         ####last in, first out
# stack.append(3)
# print(stack)
# stack.pop()
# print(stack)
# stack.pop()
# print(stack)

from collections import deque
stack=deque()

stack.append("a")
stack.append("b")
stack.append("c")
print(stack)
stack.pop()
stack.pop()
print(stack)
