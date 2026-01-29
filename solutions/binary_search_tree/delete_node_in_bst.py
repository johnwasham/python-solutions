"""
Delete Node in a BST
Medium

You are given a root node reference of a BST and a key, delete the node with the given key in the BST, if present. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: There can be multiple results after deleting the node, return any one of them.

Example 1:



Input: root = [5,3,9,1,4], key = 3

Output: [5,4,9,1]
Explanation: Another valid answer is:



Example 2:

Input: root = [5,3,6,null,4,null,10,null,null,7], key = 3

Output: [5,4,6,null,null,null,10,7]
Constraints:

0 <= The number of nodes in the tree <= 10,000.
-100,000 <= key, Node.val <= 100,000
All the values Node.val are unique.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_min_node(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root

        while curr and curr.left:
            curr = curr.left

        return curr


    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                min_node = self.find_min_node(root.right)
                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)

        return root
