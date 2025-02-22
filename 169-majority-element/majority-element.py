class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count, target = 0, None

        for num in nums:
            if count == 0:
                target = num
            count += 1 if target == num else -1  
        return target    

            #Boyer-Moore Voting Algorithm  
        