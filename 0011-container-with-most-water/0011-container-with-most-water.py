# class Solution:
    # def maxArea(self, height: list[int]) -> int:
    #     max_water=0
    #     for i in range(len(height)):
    #         for j in range(i+1,len(height)):
    #             width=j-i
    #             h=min(height[i],height[j])
    #             area=width*h
    #             if area>max_water:
    #                 max_water=area
    #     return max_water
class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            width = right - left
            h = min(height[left], height[right])

            water = width * h

            if water > max_water:
                max_water = water

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water