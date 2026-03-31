class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        newS = []

        for c in s:
            if c.isalnum():
                newS.append(c)

        left, right = 0, len(newS)-1
        
        while left < right:
            print(newS[left], "+", s[right])
            if(newS[left].lower() != newS[right].lower()):
                return False
            
            left+=1
            right-=1

        return True