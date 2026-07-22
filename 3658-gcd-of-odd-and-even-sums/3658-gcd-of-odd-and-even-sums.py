class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = 0
        sumEven = 0     #0
        odd = 1         #1
        even = 2        #2
        for i in range(n):
            sumOdd += odd #0+1=1,1+3=4
            odd += 2   #1+2=3,3+2=5
        for i in range(n):
            sumEven += even #0+2=2 2+4=6
            even += 2       #2+2=4 6+2=8
        while sumEven != 0: #t
            temp = sumEven  
            sumEven = sumOdd % sumEven
            sumOdd = temp
        return sumOdd