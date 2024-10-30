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