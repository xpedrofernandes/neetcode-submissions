class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # set of values we've already encountered
        seen = set()

        for num in nums:
            # if we've seen this number before, it's a duplicate
            if num in seen:
                return True
            # otherwise, remember it for future iterations
            seen.add(num)

        # no duplicates found
        return False            