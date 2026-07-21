class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        l=[]

        while(n!=0):
            r=n%2
            l.insert(0,r)
            n=n//2
        for i in range(1,len(l)):
            if (l[i-1]==l[i]):
                return False
        return True