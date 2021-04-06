class Solution(object):
    def minOperations(self, n):
        mid = n/2
        
        if n%2 == 0:
            return mid*mid
        else:
            return mid*(mid+1)