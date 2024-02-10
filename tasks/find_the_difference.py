class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        t = list(t)
        for letter in s:
            if letter in t:
                t.remove(letter)
            else:
                return letter

        return t[-1]