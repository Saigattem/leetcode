class Solution:
    def isHappy(self, n: int) -> bool:
        v=set()             #v=empty set
        while n!=1:         #19!=1
            if n in v:      #19 in v{}
                return False #false
            v.add(n)         #now v={19}
            total=0          #total=0 initially
            while n>0:       #19>0         #1>0
                d=n%10       #d=19%10=9    #1%10
                total=total+d*d #0+9*9=81  #81+1*1=82
                n=n//10       #19//10=1  1//10=0 loop stops
            n=total 
        return True