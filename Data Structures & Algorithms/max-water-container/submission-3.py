class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1
        max_area = min(heights[left], heights[right]) * (right - left)
        while(left < right):
            current = min(heights[left], heights[right]) * (right - left)
            max_area = max(current, max_area)

            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
            
        return max_area