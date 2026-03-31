class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freqmap = {}
        candidates = []
        for num in nums:
            if num not in freqmap:
                freqmap[num] = 1
        
        for num in freqmap.keys():
            if (num - 1) not in freqmap:
                candidates.append(num)

        longest = 0

        for candidate in freqmap:
            length = 0
            while candidate in freqmap:
                length+=1
                candidate+=1

            if length > longest:
                longest = length
        return longest
