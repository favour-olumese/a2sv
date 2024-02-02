class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        diff = 0
        difference = False
        merged_word = ''
        if len(word1) != len(word2):
            diff = min(len(word1), len(word2))
            difference = True
        else:
            diff = len(word1)

        for i in range(diff):
            merged_word += word1[i]
            merged_word += word2[i]

        if difference:
            if len(word1) > len(word2):
                merged_word += word1[diff:]
            else:
                merged_word += word2[diff:]

        return merged_word