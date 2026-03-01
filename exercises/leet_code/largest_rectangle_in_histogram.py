"""
Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height
where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

"""


def largestRectangleArea(heights: list[int]) -> int:
    stack = []
    max_area = 0
    
    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            height = heights[stack[-1]]
            stack.pop()
            width = i - stack[-1] - 1 if stack else i
            
            max_area = max(max_area, width * height)
        stack.append(i)
    
    if stack:
        right_boarder = len(heights)
        while stack:
            height = heights[stack.pop()]
            width = right_boarder - stack[-1] - 1 if stack else right_boarder
            
            max_area = max(max_area, width * height)
    
    return max_area


heights = [2, 1, 5, 6, 2, 3]
largestRectangleArea(heights)

heights = [2, 4]
largestRectangleArea(heights)
