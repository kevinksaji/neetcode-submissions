class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # create dictionary that stores numbers already covered as keys, and indices as values

        num_dict = {}

        for i in range(len(nums)):
            # check if complement to target is in num_dict
            complement = target - nums[i]
            if complement in num_dict:
                return [num_dict[complement], i]
            else:
                num_dict[nums[i]] = i
            

