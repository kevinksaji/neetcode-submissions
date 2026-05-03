class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        res = {}
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in res:
                return [res[complement] + 1, i + 1]
            else:
                res[numbers[i]] = i
        
                

