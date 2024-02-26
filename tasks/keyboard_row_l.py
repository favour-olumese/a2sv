class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = set("qwertyuiop")
        second = set("asdfghjkl")
        third = set("zxcvbnm")

        output = []
        for word in words:
            word_set = set(word.lower())
            if word_set.issubset(first) or word_set.issubset(second) or word_set.issubset(third):
                output.append(word)

        return output