class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        if len(s)%2 != 0 or len(s) == 0:
            return False 
        
        vowellist = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        mid = len(s)//2

        word1 = s[:mid]
        
        word2 = s[mid:]
        
        counter1, counter2 = 0,0 
        
        for i in word1:
            if i in vowellist:
                counter1+=1
        for i in word2:
            if i in vowellist:
                counter2+=1 
                
        return counter1 == counter2