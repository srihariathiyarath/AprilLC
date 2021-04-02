class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        x = []
        for k,v in collections.Counter(A).items():
            if v ==1:
                x.append(k)
        if len(x) == 0:
            return -1
        else:
            return max(x)


"""
	Count the frequency of all elements then get the maximum value with the frequency of 1
	Time: O(N)
	Space: O(N)
"""