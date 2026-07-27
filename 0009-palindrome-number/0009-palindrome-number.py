class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        org = x #121
        reverse = 0  #0, 121
        while x > 0: #121>0=>T
            digit = x % 10 #121%10=1
            reverse = reverse * 10 + digit #0*10=1=1
            x = x // 10 #121//10=12
        return org == reverse