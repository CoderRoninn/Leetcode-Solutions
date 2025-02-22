class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr: List[int], arr2: List[int]) -> List[int]:
            pointer1, pointer2 = 0, 0
            merged = []

            while pointer1 < len(arr) and pointer2 < len(arr2):
                if arr[pointer1] < arr2[pointer2]:
                    merged.append(arr[pointer1])
                    pointer1 += 1
                else:
                    merged.append(arr2[pointer2])
                    pointer2 += 1
            while pointer1 < len(arr):
                merged.append(arr[pointer1])
                pointer1 += 1
            while pointer2 < len(arr2):
                merged.append(arr2[pointer2])
                pointer2 += 1

            return merged 
        def merge_sort(arr: List[int]) -> list[int]:
            if len(arr) == 1:
                return arr

            middle = len(arr) // 2
            left = arr[:middle]
            right = arr[middle:]

            return merge(merge_sort(left), merge_sort(right))
        return merge_sort(nums)   
        