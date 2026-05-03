class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res: List[List[int]] = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue  # skip same anchor

            l, r = i + 1, len(nums) - 1
            while l < r:
                curr = a + nums[l] + nums[r]
                if curr < 0:
                    l += 1
                elif curr > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    # move both pointers first
                    l += 1
                    r -= 1
                    # skip duplicates on the left
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # skip duplicates on the right
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return res

            

