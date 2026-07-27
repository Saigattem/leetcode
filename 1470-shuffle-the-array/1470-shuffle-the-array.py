class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans=[]                     # 0 1 2 3 4 5   
        for i in range(n):         #[2,5,1,3,4,7]
            ans.append(nums[i])#x=>i=0[2]
            ans.append(nums[i+n])#y=>i=0 0+3=i[3]=>3
        return ans