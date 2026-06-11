# Definition for a binary tree node.
  # class TreeNode:
  #     def __init__(self, val=0, left=None, right=None):
  #         self.val = val
  #         self.left = left
  #         self.right = right
  
class Solution:
      def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:                                                                                               
          n = len(preorder)
          idx_of = {v: i for i, v in enumerate(inorder)}  # value -> inorder index
          placed = [None] * n                             # dummy list mirroring inorder

          root = TreeNode(preorder[0])
          placed[idx_of[preorder[0]]] = root

          for val in preorder[1:]:
              i = idx_of[val]
              node = TreeNode(val)
                                                                                                                                                                                        
              # nearest already-placed node to the left
              L = None
              for j in range(i - 1, -1, -1):
                  if placed[j] is not None:
                      L = placed[j]
                      break
                                                                                                                                                                                        
              # nearest already-placed node to the right
              R = None
              for j in range(i + 1, n):
                  if placed[j] is not None:
                      R = placed[j]
                      break
                                                                                                                                                                                        
              # parent is L or R: exactly one facing child slot is free
              if L is not None and L.right is None and (R is None or R.left is not None):
                  L.right = node
              else:
                  R.left = node
  
              placed[i] = node

          return root
