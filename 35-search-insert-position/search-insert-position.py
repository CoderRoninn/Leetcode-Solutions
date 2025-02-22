class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) -1

        while right >= left:
            middle = left + (right-left) //2

            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                left = middle +1
            else:
                right = middle -1
        return left        


        