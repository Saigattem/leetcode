
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        h=len(nums) - 1
        ans1=-1
        while l<=h:
            mid = (l+h)//2
            if nums[mid]==target:
                ans1 = mid
                h = mid - 1      
            elif nums[mid] < target:
                l = mid + 1
            else:
                h = mid - 1
        l1=0
        h1=len(nums)-1
        ans2=-1
        while l1<=h1:
            mid=(l1+h1)//2
            if nums[mid]==target:
                ans2=mid
                l1=mid+1     
            elif nums[mid]<target:
                l1=mid+1
            else:
                h1=mid-1
        return [ans1,ans2]