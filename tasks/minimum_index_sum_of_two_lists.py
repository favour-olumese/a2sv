class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_num = 2000
        result = []
        for index, value in enumerate(list1):
            if value in list2:
                summation = index + list2.index(value)
                if summation < index_num:
                    index_num = summation
                    result.clear()
                    result.append(value)
                elif summation == index_num:
                    result.append(value)
                

        return result