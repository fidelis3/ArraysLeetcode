def maxArea(height):
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        # Calculate width
        width = right - left
        
        # Find the smaller height
        h = min(height[left], height[right])
        
        # Calculate area
        area = h * width
        max_area = max(max_area, area)
        
        # Move the pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area
# Example usage:
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))