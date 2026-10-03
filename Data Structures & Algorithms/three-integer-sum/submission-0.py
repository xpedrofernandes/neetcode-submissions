class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # initialize an empty list to collect the answers, since the answer is a collection of items
        res = []
        # Sort so two pointers work (move l up if sum too small, r down if too big)
        # and duplicates sit adjacent for easy skipping. 
        nums.sort()

        # use enumerate to get the index and value of each element 
        for i, a in enumerate(nums):
            # if a > 0, the sum is never gonna be 0, it's always gonna increase
            if a > 0:
                break

            # if i is not first element and the element before it is the same, go to next iteration 
            if i > 0 and a == nums[i - 1]:
                continue
            
            # initialize two pointers
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r] 
                if threeSum > 0: # if the sum is more than 0, move right pointer to element before, which will be smaller
                    r -= 1
                elif threeSum < 0: # same principle: if sum is less than 0, move pointer to element after, which will be bigger
                    l += 1
                else: # if sum is 0, append answer and update pointers
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]: # duplicate skipping - keep advancing l as long as nums[l] equals the value before it 
                        l += 1
        
        return res 

