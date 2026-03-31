class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = [1]
        n = len(nums)
        res = [1] * n

        # LEFT PRODUCTS
        left = 1
        for i in range(n):
            res[i] = left
            left *= nums[i]

        # RIGHT PRODUCTS
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res
