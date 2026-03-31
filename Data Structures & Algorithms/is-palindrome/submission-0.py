class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=''
        for i in s:
            if i.isalnum():
                st += i.lower()
        for i in range(int(len(st)/2)):
            print(i)
            if(st[i]!=st[-i-1]):
                return False
        return True