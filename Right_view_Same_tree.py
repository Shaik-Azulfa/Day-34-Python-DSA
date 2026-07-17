from collections import deque

class Solution:
    def rightView(self, root):
        if not root:
            return []

        result = []
        q = deque([root])

        while q:
            level_size = len(q)
            for i in range(level_size):
                node = q.popleft()
                # last node of this level
                if i == level_size - 1:
                    result.append(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return result
class Solution:
    def isIdentical(self, root1, root2):
        # Both are None
        if not root1 and not root2:
            return True
        # One is None
        if not root1 or not root2:
            return False
        # Data should be same and subtrees should also be same
        return (root1.data == root2.data and
                self.isIdentical(root1.left, root2.left) and
                self.isIdentical(root1.right, root2.right))
