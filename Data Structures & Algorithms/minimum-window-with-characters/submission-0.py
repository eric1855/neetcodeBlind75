class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for c in t:
            need[c] = 1 + need.get(c, 0)
                                                                                                                                                                                                              
        have, required = 0, len(need)  # count distinct chars fully satisfied                                                                                                                               
        window = {}                                                                                                                                                                                         
        res, resLen = [-1, -1], float("inf")                                                                                                                                                                
        l = 0                                                                                                                                                                                               
   
        for r in range(len(s)):                                                                                                                                                                             
            c = s[r]
            window[c] = 1 + window.get(c, 0)                                                                                                                                                                
                  
            # if this char is now fully satisfied, increment have                                                                                                                                           
            if c in need and window[c] == need[c]:
                have += 1                                                                                                                                                                                   
                                                                                                                                                                                                              
            # shrink from left while window is valid
            while have == required:                                                                                                                                                                         
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1                                                                                                                                                                      
   
                # remove s[l] from window                                                                                                                                                                   
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1                                                                                                                                                                               
                l += 1
                                                                                                                                                                                                              
        l, r = res
        return s[l:r + 1] if resLen != float("inf") else ""

