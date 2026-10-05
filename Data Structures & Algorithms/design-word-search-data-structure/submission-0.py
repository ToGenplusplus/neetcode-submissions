class TrieNode:

    def __init__(self):
        self.children: dict[TrieNode] = {}
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self._root = TrieNode()

    def addWord(self, word: str) -> None:
        # if not word or word == "":
        #     return

        curr = self._root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word = True
        

    def search(self, word: str) -> bool:

        def dfs(index: int, node: TrieNode) -> bool:
            curr = node

            for i in range(index, len(word)):

                char = word[i]

                if char == ".":

                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False

                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            
            return curr.is_end_of_word

        return dfs(0, self._root)


        """
        tree {bay, day}
        word: .ay
        dfs, 0, root
            word[i] = .
            dfs (1, b)
                word[i] = a
                a is in b.child
                curr = a, i++
                word[i] = y
                y in a.children
                curr = y, i++
                i > len(word)
                curr=y.end_of_word is true

            dfs (1,d)

        word: b..
        dfs(0, root)
            b in root.child
            curr = b, index = 1
            word[i] = .
            dfs(2,a)
                word[i] = .
                dfs(3,y)
                    3 >= len(word)
                    y.end_of_word = True -> True
        """


        