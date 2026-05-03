from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ret_arr = []
        freq = Counter(nums)
        for i in range(k):
            # get key with max value
            max_key = max(freq, key=freq.get)
            del freq[max_key]
            ret_arr.append(max_key)

        return ret_arr