class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # initialize a hashmap
        count = {}

        # initialize an array of arrays - here, the indexes are going to be the count of ocurrences of each element. in other words, the index will represent the number of times the values inside that index have appeared in nums
        freq = [[] for i in range(len(nums) + 1)]

        # populate the hashmap
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # bucket by frequency: number n belongs at index c = count[n]
        for n, c in count.items():
            freq[c].append(n)

        # create the result array
        res = []

        # iterate through the freq array in descending order. for each num in the freq array, append it to res. return once result equals k
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res