class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        print(nums)
        for idx in range(len(nums)-2):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            one = nums[idx]
            print("sum", one)
        
            left ,right = idx+1,len(nums)-1
            while left < right:
                print(nums[left], "+",nums[right])
                if nums[left] + nums[right] == -one:
                    res.append([one,nums[left],nums[right]])
                    left+=1
                    right-=1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif nums[left]+nums[right] < -one:
                    left+=1
                elif nums[left] + nums[right] > -one:
                    right-=1


        return res
        
