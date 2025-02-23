class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        insert_index = 0

        for num in nums:
            if val != num:
                nums[insert_index] = num
                insert_index += 1
        return insert_index        

        