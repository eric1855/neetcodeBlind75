# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        q = deque()
        q.append(root)

        visited = set()

        while q:
            length = len(q)
            for i in range(length):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    visited.add(node.val)
        print(visited)
        return list(visited)[k-1]
