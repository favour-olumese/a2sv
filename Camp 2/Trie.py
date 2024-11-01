# TRIES

# INSERTION IN TRIE
# https://leetcode.com/playground/jx6mSTWN

"""
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # your code goes here
        cur = self.root
        
        for char in word:
            index = ord(char) - ord('a')
            if not cur.children[index]:
                cur.children[index] = TrieNode()
                
            cur = cur.children[index]
            
        cur.is_end = True
        
        
        
        
if __name__ == "__main__":
    trie = Trie()
        
    trie.insert("hi")
    
    for i in range(26):
        if i == ord('h') - ord('a'):
            assert trie.root.children[i] != None, "expected char 'h' to be child of root, found None"
            assert isinstance(trie.root.children[i], TrieNode), f"expected TrieNode as child, found {type(trie.root.children[i]).__name__}"
        else:
            assert trie.root.children[i] == None, f"char '{chr(i + 65)}' is inserted as child of root, expected None"
            
    i_node = trie.root.children[ord('h') - ord('a')].children[ord('i') - ord('a')]
    assert isinstance(i_node, TrieNode), f"expected TrieNode as child, found {type(i_node).__name__}"
    
    assert i_node.is_end, "expected last character node to be end of word"
        
    print("Good Job!")
"""


# IMPLEMENTATION OF TRIE
# https://leetcode.com/problems/implement-trie-prefix-tree/submissions/1438149657/
"""
class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root

        for char in word:
            index = ord(char) - ord('a')

            if not current.children[index]:
                current.children[index] = TrieNode()

            current = current.children[index]

        current.is_end = True

    def search(self, word: str) -> bool:
        current = self.root

        for char in word:
            index = ord(char) - ord('a')

            if not current.children[index]:
                return False

            current = current.children[index]

        if current.is_end:
            return True

        return False

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for char in prefix:
            index = ord(char) - ord('a')

            if not current.children[index]:
                return False

            current = current.children[index]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
"""

# IMPLEMENTATION OF DELETION IN TRIE
# https://leetcode.com/playground/ewxuJkKb
# https://www.geeksforgeeks.org/introduction-to-trie-data-structure-and-algorithm-tutorials/
"""
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # your code goes here
        current = self.root
        
        
        for char in word:
            index = ord(char) - ord('a')
            
            if not current.children[index]:
                current.children[index] = TrieNode()
                
            current = current.children[index]
            
        current.is_end = True


    def delete(self, word: str) -> None:
        # your code goes here
        current = self.root
        last_branch_node = None
        last_branch_char = 'a'

        # Loop through each character in the word.
        for char in word:
            index = ord(char) - ord('a')
            
            # Return False as word is not present in Trie
            if not current.children[index]:
                return False
            
            count = 26 - current.children.count(None)
            
            if count > 1:
                last_branch_node = current
                last_branch_char = char
                
            current = current.children[index]
            
        count = 26 - current.children.count(None)
        
        # Case 1: The deleted word is a prefix of other word in Trie
        if count > 0:
            current.is_end = False
            return False
            
        # Case 2: The deleted word shares a common prefix with other words in Trie
        if last_branch_node:
            last_branch_node.children[ord(last_branch_char) - ord('a')] = None
            return True
        
        # Case 3: The deleted word does not share any common prefix with the other words in Trie (it is unique).
        else:
            root.children[ord(word[0]) - ord('a')] = None
            return True
            
        
if __name__ == "__main__":
    trie = Trie()
        
    trie.insert("hi")
    trie.insert("he")
    trie.delete("hi")
    
    for i in range(26):
        if i == ord('h') - ord('a'):
            assert trie.root.children[i] != None, "expected char 'h' to be child of root, found None"
            assert isinstance(trie.root.children[i], TrieNode), f"expected TrieNode as child, found {type(trie.root.children[i]).__name__}"
        else:
            assert trie.root.children[i] == None, f"char '{chr(i + 65)}' is inserted as child of root, expected None"
            
    i_node = trie.root.children[ord('h') - ord('a')].children[ord('i') - ord('a')]        
    assert i_node == None, f"expected i to be deleted"
    
    e_node = trie.root.children[ord('h') - ord('a')].children[ord('e') - ord('a')]
    assert isinstance(e_node, TrieNode), f"expected 'e' to exist, found None"
    
    assert e_node.is_end, "expected 'e' to be end of word"
        
    print("Good Job!")

"""
# -------------------------------------------------------------------------------
# BINARY TRIE (RADIX TREE)

# FROM CHATPGT (DSA) 01-11-2024
"""
class TrieNode:
    def __init__(self):
        self.left = None  # Represents '0' bit
        self.right = None  # Represents '1' bit

class BinaryTrie:
    def __init__(self):
        self.root = TrieNode()

    # Insert a number into the binary trie
    def insert(self, num):
        node = self.root
        # Traverse the bits of the number from the most significant to the least significant
        for i in range(31, -1, -1):  # 32-bit integer representation
            bit = (num >> i) & 1  # Extract the ith bit from the left
            if bit == 0:
                if not node.left:
                    node.left = TrieNode()
                node = node.left
            else:
                if not node.right:
                    node.right = TrieNode()
                node = node.right

    # Search if a number exists in the trie
    def search(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit == 0:
                if not node.left:
                    return False
                node = node.left
            else:
                if not node.right:
                    return False
                node = node.right
        return True

    # Find the maximum XOR for a given number with any number in the trie
    def find_max_xor(self, num):
        node = self.root
        max_xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            # Try to go opposite to maximize the XOR
            if bit == 0:
                if node.right:  # If we can go to '1'
                    max_xor |= (1 << i)  # Set the ith bit of result to 1
                    node = node.right
                else:
                    node = node.left
            else:
                if node.left:  # If we can go to '0'
                    max_xor |= (1 << i)  # Set the ith bit of result to 1
                    node = node.left
                else:
                    node = node.right
        return max_xor

        
    # Find the minimum XOR for a given number with any number in the trie
    def find_min_xor(self, num):
        node = self.root
        min_xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            # Try to follow the same path to minimize the XOR
            if bit == 0:
                if node.left:  # If we can go to '0'
                    node = node.left
                else:
                    min_xor |= (1 << i)  # Set the ith bit of result to 1
                    node = node.right
            else:
                if node.right:  # If we can go to '1'
                    node = node.right
                else:
                    min_xor |= (1 << i)  # Set the ith bit of result to 1
                    node = node.left
        return min_xor

        
# Example usage:
trie = BinaryTrie()
nums = [5, 9, 25]  # Binary representations: 5 -> 0101, 9 -> 1001, 25 -> 11001
for num in nums:
    trie.insert(num)

print("Searching for 5:", trie.search(5))  # True
print("Searching for 15:", trie.search(15))  # False

# Find the maximum XOR of 5 with any number in the trie
print("Max XOR with 5:", trie.find_max_xor(5))  # Should return 25 XOR 5 = 28
"""

# PERSONAL REFACTORING OF CHATGPT IMPLEMENTATION 
# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/submissions/1440180425/
"""
class TrieNode:
    def __init__(self):
        self.left = None # Represents '0' bit.
        self.right = None # Represents '1' bit.

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        current = self.root

        binary = bin(num)[2:]
        binary_32 = ('0' * (32 - len(binary))) + binary

        for bit in binary_32:
            if bit == '0':
                if not current.left:
                    current.left = TrieNode()
                current = current.left

            if bit == '1':
                if not current.right:
                    current.right = TrieNode()
                current = current.right

    def find_max_xor(self, num):
        current = self.root

        binary = bin(num)[2:]
        binary_32 = ('0' * (32 - len(binary))) + binary
        max_xor = ['0'] * 32
        i = 0
        for bit in binary_32:

            # We would try to go the opposite direction to maximize the XOR
            if bit == '0':
                if current.right: # If we can go to 1
                    max_xor[i] = '1' # Set the ith bit to 1
                    current = current.right

                else:
                    current = current.left

            else:
                if current.left: # If we can to 0
                    max_xor[i] = '1' # Set the ith bit to 1
                    current = current.left

                else:
                    current = current.right

            i += 1
            
        return int(''.join(max_xor), 2)


    def findMaximumXOR(self, nums: List[int]) -> int:
        nums = list(set(nums))
        maxi = 0
        for num in nums:
            self.insert(num)

        for num in nums:
            maxi = max(self.find_max_xor(num), maxi)

        return maxi
"""