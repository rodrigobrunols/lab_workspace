# import collections
# from typing import List
#
#
# class TreeNode:
#
#     def __init__(self, data, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right
#
#     # Time: O(log(n)) Space: O(1)
#     def insert(self, data):
#         if data < self.data:
#             if self.left is None:
#                 self.left = TreeNode(data)
#             else:
#                 self.left.insert(data)
#         elif data > self.data:
#             if self.right is None:
#                 self.right = TreeNode(data)
#             else:
#                 self.right.insert(data)
#         else:
#             self.data = data
#
#     # Time: O(n) Space: O(1)
#     def inorder_traversal(self):
#         if self.left:
#             self.left.inorder_traversal()
#         print(self.data)
#         if self.right:
#             self.right.inorder_traversal()
#
#     # Time: O(n) Space: O(1)
#     def preorder_traversal(self):
#         print(self.data)
#         if self.left:
#             self.left.preorder_traversal()
#         if self.right:
#             self.right.preorder_traversal()
#
#     # Time: O(n) Space: O(1)
#     def postorder_traversal(self):
#         if self.left:
#             self.left.postorder_traversal()
#         if self.right:
#             self.right.postorder_traversal()
#         print(self.data)
#
#     # Time: O(log(n)) Space: O(1)
#     def find(self, data):
#         if data < self.data:
#             if self.left is None:
#                 return False
#             else:
#                 return self.left.find(data)
#         elif data > self.data:
#             if self.right is None:
#                 return False
#             else:
#                 return self.right.find(data)
#         else:
#             return True
#
#     # Time O(n) Space(O(n))
#     def level_traversal(self) -> List:
#
#         q = collections.deque()
#
#         q.append(self)
#
#         while q:
#             node = q.popleft()
#
#             if node:
#                 print(node.data)
#                 q.append(node.left)
#                 q.append(node.right)
#
# #
# #
# #
# # Time O(n) Space(O(n))
# def bfs(root: TreeNode) -> List:
#     result = []
#
#     q = collections.deque()
#     q.append(root)
#
#     while len(q) > 0:
#         node = q.popleft()
#
#         if node:
#             result.append(node.data)
#             q.append(node.left)
#             q.append(node.right)
#
#     return result
#
#
#
#
#
# a = TreeNode(8)
# a.insert(5)
# a.insert(15)
# a.insert(12)
# a.insert(4)
# a.insert(6)
# a.insert(16)
#
#
# print("inorder_traversal")
# a.inorder_traversal()
# print("preorder_traversal")
# a.preorder_traversal()
# print("postorder_traversal")
# a.postorder_traversal()
# print("level_traversal")
# a.level_traversal()
# print("find")
# print(a.find(30))
# print("bfs")
# print(bfs(a))
#
#
print(int(9/-2))

import math

value = 10.6
truncated_value = math.trunc(value)
print(truncated_value)  # Output: 10

value = 10.6
truncated_value = int(value)
print(truncated_value)  # Output: 10

value = 10.6
truncated_value = value // 1
print(int(truncated_value))  # Output: 10
