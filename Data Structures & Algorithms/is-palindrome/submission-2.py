class Solution:
    def isPalindrome(self, s: str) -> bool:
        # build using list instead of +=
        chars = []
        for i in s:
            if i.isalnum():
                chars.append(i.lower())
        
        st = ''.join(chars)  # O(n) instead of O(n^2)
        
        # compare halves
        for i in range(len(st) // 2):
            if st[i] != st[-i - 1]:
                return False
        return True
