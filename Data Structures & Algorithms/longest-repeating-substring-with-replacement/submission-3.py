class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        bestLength = 0
        res = 0

        l = 0

        for r in range(len(s)):
            print(l,r)
            freq[s[r]] = 1 + freq.get(s[r],0)
            bestLength = max(bestLength, freq[s[r]])

            while r-l+1 - bestLength > k:
                freq[s[l]] -= 1
                l += 1
            res = max(r-l+1,res)

        return res
        
