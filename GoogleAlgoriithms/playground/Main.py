from collections import deque

stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)

last = stack.pop()
first = stack.popleft()

print(first)
print(last)

