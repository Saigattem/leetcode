class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s=sorted(s)  #Before:s = "anagram" After sorting:s = ['a','a','a','g','m','n','r']
        # t=sorted(t)  #Before:t = "nagaram"After sorting:t = ['a','a','a','g','m','n','r']
        # if s==t:  #s==t
        #     return True #true

        # return False
        return sorted(s)==sorted(t)