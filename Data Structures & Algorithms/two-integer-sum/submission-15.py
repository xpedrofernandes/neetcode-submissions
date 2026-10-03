class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hashmap to store value and index, because it allows for O(1) lookups by value. We end up having to loopup by index, so at the end it will cost O(n). 
        indices = {}

        # establish the number to be found and check if it is in the indices array
        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices:
                return [indices[diff], i] # if diff has been seen before, we found the pair
            indices[n] = i # if we did not find it, remember n for future iterations. 
        
        return [] # return empty list if needed
            