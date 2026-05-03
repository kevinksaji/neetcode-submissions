
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # hash map with key as num, value as number of occurences
        count = {}

        # array of arrays. each index will be the count, then all the nums of that
        # count will be at that index in the list
        freq = [[] for i in range(len(nums) + 1)]

        # create frequency hash map, key is num, value is number of occurences
        for n in nums:
            count[n] = 1+ count.get(n, 0)

        # for each value, append the number to the index
        for n, c in count.items():
            freq[c].append(n)

        res = []

        # iterate over freq in reverse
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res




