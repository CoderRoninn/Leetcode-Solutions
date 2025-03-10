class Solution:
    def romanToInt(self, s: str) -> int:


        my_dict = {"M": 1000, "D": 500,
                   "C": 100, "L": 50,
                   "X": 10, "V": 5,
                   "I": 1}
         
        num, i = 0, 0
         
        while i < len(s):
            if i+1 < len(s) and my_dict[s[i]] < my_dict[s[i+1]]:
                num += my_dict[s[i+1]] - my_dict[s[i]]
                i += 2
            else:
                num += my_dict[s[i]]
                i += 1

        return num          
         
        
             
        
       
                    
        
            
    
   
        