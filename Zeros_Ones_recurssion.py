class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:  
        
        def findMax(strs, i, m, n):
            counter = 0
            if i <= len(strs)-1: 
                if m > 0 or n > 0:
                    # use it or skip it
                    m1 = strs[i].count('0')
                    n1 = strs[i].count('1')
                    use = 0
                    
                    # skip it
                    skip = findMax(strs, i+1, m, n)
                    
                    # use it
                    if m1 <= m and n1 <= n:
                        use = findMax(strs, i+1, m-m1, n-n1) + 1
                    
                    # update counter
                    counter = max(use, skip)
                                
            return counter
            
        counter = findMax(strs, 0, m, n)
        return counter