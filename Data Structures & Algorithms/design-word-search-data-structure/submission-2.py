class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self._root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self._root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.is_word = True
        

    def search(self, word: str) -> bool:

        def find_word(node: TrieNode, index: int) -> bool:
            curr = node

            for i in range(index, len(word)):

                c = word[i]

                if c == ".":

                    for child in curr.children.values():
                        if find_word(child, i + 1):
                            return True
                    return False
                else:

                    if c not in curr.children:
                        return False
                    curr = curr.children[c]

            return curr.is_word

        return find_word(self._root, 0)
