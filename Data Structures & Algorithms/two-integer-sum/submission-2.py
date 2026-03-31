class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            a = target-nums[i]
            if a in nums[i+1:]:
                nums[i]=-999
                return [i,nums.index(a)]