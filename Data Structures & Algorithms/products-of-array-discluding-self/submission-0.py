class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = [1] * len(nums)

        # --- Prefix Pass (left to right) ---
        # prefix holds the product of all elements to the LEFT of index i.
        # We assign res[i] = prefix BEFORE multiplying nums[i] into prefix,
        # so nums[i] is naturally excluded from the left-side product.
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # --- Postfix Pass (right to left) ---
        # postfix holds the product of all elements to the RIGHT of index i.
        # Same logic: we multiply res[i] by postfix BEFORE including nums[i],
        # so nums[i] is excluded from the right-side product.
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        # res[i] now contains (product of left) * (product of right) = product except self
        return res