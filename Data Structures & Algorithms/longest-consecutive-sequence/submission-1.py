class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dc = {}
        for i in nums:
            dc[i] = [False,False]
        
        for i in dc:
            if i-1 in dc:
                dc[i][0] = True
            if i+1 in dc:
                dc[i][1] = True

        start = []
        for i in dc:
            if dc[i] == [False,True] or dc[i] == [False, False]:
                start.append(i)

        out = 0
        for i in start:
            cnt = 1
            iterator = i
            flag = False
            while not flag:
                if dc[iterator][1] == True:
                    iterator += 1
                    cnt += 1
                else:
                    flag = True
            out = max(cnt, out)
        return out
