class Solution:
    def reverseWords(self, s: str) -> str:
        import re

        match = re.findall('\w+', s)
        return(' '.join(match[::-1]))