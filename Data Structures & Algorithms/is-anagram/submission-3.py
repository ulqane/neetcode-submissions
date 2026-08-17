class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letterS, letterT = {}, {}

        for x in range(len(s)):
            letterS[s[x]] = 1 + letterS.get(s[x],0)
            letterT[t[x]] = 1 + letterT.get(t[x],0)

        return letterS == letterT