class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        for l in range(len(heights)-1):
            r = l+1
            while r < (len(heights)):
                if (min(heights[l],heights[r])*(r-l) > max):
                    max = min(heights[l],heights[r])*(r-l)
                r+=1
            
        return max
                

