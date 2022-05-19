# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n
        while l<=r:
            m = int((l+r)/2)
            if not isBadVersion(m-1) and isBadVersion(m):
                return m
            elif isBadVersion(m):
                r = m-1
            else:
                l = m+1
        return -1
        
