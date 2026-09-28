class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert the array into a set. A set is great for searching and handles the duplicates
        numSet = set(nums)
        longest = 0

        # iterate through each number in the set
        for n in numSet:
            # if the number that comes mathematically before the one we are checking is not in the set, then this could be the beginning of a sequence. only then we will move on. 
            if (n - 1) not in numSet: 
                streak = 0
                # keep adding to the number to see where the streak goes
                while (n + streak) in numSet:
                    streak += 1
                longest = max(streak, longest)
        
        # return the longest sequence
        return longest