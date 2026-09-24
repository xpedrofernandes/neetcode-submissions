class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # check if they are of same size. if not, return false
        if len(s) != len(t):
            return False

        # create hashmaps countS and countT
        countS, countT = {}, {}

        # populate these hashmaps, using .get() in case the key doesnt exist
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # check if each component of countS matches countT
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True