"""
Binary Tree Level Order Traversal
Medium
Company Tags
Hints
Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.

Example 1:



Input: root = [1,2,3,4,5,6,7]

Output: [[1],[2,3],[4,5,6,7]]
Example 2:

Input: root = [1]

Output: [[1]]
Example 3:

Input: root = []

Output: []
Constraints:

0 <= The number of nodes in the tree <= 1000.
-1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


# mine - uses 2 queues, not bad, same O(n) space

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q_children = deque()
        result = []
        temp = []

        if root is None:
            return []

        q.append(root)

        while q:
            node = q.popleft()

            temp.append(node.val)
            if node.left:
                q_children.append(node.left)
            if node.right:
                q_children.append(node.right)

            if not q:
                result.append(temp[:])
                temp = []
                # load kids into q
                while q_children:
                    q.append(q_children.popleft())

        return result

# theirs - better, of course

from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        result = []

        if root is None:
            return []

        q.append(root)

        while q:
            q_len = len(q)
            level = []

            for i in range(q_len):
                node = q.popleft()

                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                result.append(level)

        return result
