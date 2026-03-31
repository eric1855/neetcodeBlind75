class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = dict.fromkeys(set(s),0)
        st = dict.fromkeys(set(t),0)

        for i in s:
            sd[i] += 1
        for j in t:
            st[j] += 1

        if sd == st:
            return True
        return False