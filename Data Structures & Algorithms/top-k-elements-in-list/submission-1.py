class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = defaultdict(int)
        for i in nums:
            dct[i] += 1
        
        arr = []
        for key,val in dct.items():
            arr.append([val,key])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res