class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        post = [1]
        for i in range(1,len(nums)):
            pre.append(pre[i-1]*nums[i-1])
            post.append(post[i-1]*nums[-i])
        print(pre)
        print(post)

        res = []
        for i in range(len(nums)):
            res.append(pre[i]*post[-i-1])
        return res