from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
            
        freq_s = Counter(s)
        freq_t = Counter(t)
        

        for value in freq_s:
            if freq_s[value] != freq_t[value]:
                return False
        return True
        