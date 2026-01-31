
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# O(n) time, O(height) space
def inorder_iterative(node):
    stack = []
    curr = node

    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            print(curr.val)
            curr = curr.right


# O(n) time, O(height) space
def preorder_iterative(node):
    stack = []
    curr = node

    while curr or stack:
        if curr:
            print(curr.val)
            if curr.right:
                stack.append(curr.right)
            curr = curr.left
        else:
            curr = stack.pop()


# O(n) time, O(height) space
def postorder_iterative(node):
    stack = [node]
    visit = [False]

    while stack:
        curr, visited = stack.pop(), visit.pop()
        if curr:
            if visited:
                print(curr.val)
            else:
                stack.append(curr)
                visit.append(True)
                stack.append(curr.right)
                visit.append(False)
                stack.append(curr.left)
                visit.append(False)

