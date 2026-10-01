class TreeNode:
    def __init__(self):
        self.end_of_word = False
        self.children: dict[str: TreeNode] = {}

class PrefixTree:

    def __init__(self):
        self._root = TreeNode()

    def insert(self, word: str) -> None:
        if not word:
            return 

        curr = self._root
        for char in word:
            if not char in curr.children:
                curr.children[char] = TreeNode()
            curr = curr.children[char]

        curr.end_of_word = True


    def search(self, word: str) -> bool:
        if not word:
            return False

        curr = self._root
        for char in word:
            if not char in curr.children:
                return False
            curr = curr.children[char]
        
        return curr.end_of_word
        

    def startsWith(self, prefix: str) -> bool:
        
        if not prefix:
            return False

        curr = self._root
        for char in prefix:
            if not char in curr.children:
                return False
            curr = curr.children[char]
        
        return True
        