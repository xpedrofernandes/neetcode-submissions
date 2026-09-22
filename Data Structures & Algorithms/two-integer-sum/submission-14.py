class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        
        # create a hashmap
        indices = {}

        # map each value to its index
        for i, n in enumerate(nums):
            indices[n] = i

        # establish the number to be found and check if it is in the indices array and it is not equal to i
        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        
        return [] # return empty list if needed
            