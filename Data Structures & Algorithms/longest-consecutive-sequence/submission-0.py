class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        hSet = set(nums)
        maxSeq = 0

        for num in hSet:
            # start of a new sequence
            if num - 1 not in hSet:
                curr = num
                seq = 1  # include the current number

                while curr + 1 in hSet:
                    curr += 1
                    seq += 1

                maxSeq = max(maxSeq, seq)

        return maxSeq