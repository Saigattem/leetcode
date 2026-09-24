class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # if n<=0:  #27<=0
        #   return False
        # while n%3==0: #27%3=0
        #     n=n//3    #27//3=9
        # return n==1
        if n <= 0:
            return False
        for i in range(n):
            if n==1:
                return True
            if n%3!=0:
                return False

            n=n//3

        return True

