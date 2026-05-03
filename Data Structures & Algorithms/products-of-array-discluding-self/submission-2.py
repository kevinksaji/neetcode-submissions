class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        output = [1] * length

        pre = [1] * length

        suf = [1] * length

        for i in range(len(nums)):
            
            if i != 0:
                pre[i] = pre[i-1] * nums[i-1]

        for i in range(len(nums)-1, -1, -1):
            
            if i != length -1:
                suf[i] = suf[i+1] * nums[i+1]


        for i in range(len(nums)):
            output[i] = pre[i] * suf[i]


        return output
