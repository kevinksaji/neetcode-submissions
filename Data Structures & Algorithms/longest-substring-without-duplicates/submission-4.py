from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        currSet = {} # create dictionary with keys as characters, values as indexes
        maxLength = 0 # set maxLength to negative infinity initially
        start = 0 # set start index of substring to 0

        # move the end index of substring
        for index, char in enumerate(s):

            # if duplicate is found, get index of duplicate in current substring and set start to the next index
            if char in currSet:
                prevIndex = currSet[char]
                if prevIndex >= start:
                    start = prevIndex + 1

            currSet[char] = index

            # get the currentLength and update maxLength
            currLength = index - start + 1
            maxLength = max(currLength, maxLength)

        return maxLength

                


        
            


