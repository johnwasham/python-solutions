"""
Insert into a Binary Search Tree
Medium

You are given the root node of a binary search tree (BST) and a value val to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Note: There may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

Example 1:



Input: root = [5,3,9,1,4], val = 6

Output: [5,3,9,1,4,6]
Example 2:

Input: root = [5,3,6,null,4,null,10,null,null,7], val = 9

Output: [5,3,6,null,4,null,10,null,null,7,null,null,9]
Constraints:

0 <= The number of nodes in the tree <= 10,000.
-100,000,000 <= val, Node.val <= 100,000,000
All the values Node.val are unique.
It's guaranteed that val does not exist in the original BST.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current = root

        if current is None:
            root = TreeNode(val)
            return root

        while current is not None:
            if val < current.val:
                if current.left is None:
                    current.left = TreeNode(val)
                    break
                else:
                    current = current.left
            elif val > current.val:
                if current.right is None:
                    current.right = TreeNode(val)
                    break
                else:
                    current = current.right

        return root
