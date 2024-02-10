class Solution:
    def freqAlphabets(self, s: str) -> str:
        list_items = []
        i = 1
        result = ''
        while i < len(s) + 1:
            if s[-i] == '#':
                list_items.append(s[-(i+2):-i])
                i += 3
            else:
                list_items.append(s[-i])
                i += 1
        print(list_items)
        for i in range(len(list_items)):
            result += chr(96 + int(list_items[-(i+1)]))

        return result