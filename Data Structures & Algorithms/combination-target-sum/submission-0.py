class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(index, total, path):
            
            if index == len(nums) or total > target:
                return
            
            if total == target:
                result.append(path[:])
                return

            path.append(nums[index])
            backtrack(index, total + nums[index], path)

            path.pop()
            backtrack(index + 1, total, path)
            return
        
        backtrack(0,0,[])
        return result