class TrieNode:
    def __init__(self, value):
        self.isLast = False
        self.value = value
        self.child = []

class Trie:

    def __init__(self):
        self.rootNode = TrieNode("*")

    def insert(self, word: str) -> None:
        tempNode = self.rootNode
        tempWord = word
        while(tempWord != ""):
            c = tempWord[0]
            matching_child = [x for x in tempNode.child if x.value == c]
            if len(matching_child) == 0:
                newNode = TrieNode(c)
                if len(tempWord) == 1:
                    # print(tempWord)
                    newNode.isLast = True
                tempNode.child.append(newNode)
                tempNode = newNode
            else:
                if len(tempWord) == 1:
                    print(tempWord)
                    matching_child[0].isLast = True
                tempNode = matching_child[0]
            tempWord = tempWord[1:]

    def search(self, word: str) -> bool:
        tempNode = self.rootNode
        tempWord = word
        while(tempWord != ""):
            c = tempWord[0]
            matching_child = [x for x in tempNode.child if x.value == c]
            if len(matching_child) == 0:
               return False
            if len(tempWord) == 1:
                return matching_child[0].isLast
            tempNode = matching_child[0]
            tempWord = tempWord[1:]
        return True

    def startsWith(self, prefix: str) -> bool:
        tempNode = self.rootNode
        tempWord = prefix
        while(tempWord != ""):
            c = tempWord[0]
            matching_child = [x for x in tempNode.child if x.value == c]
            if len(matching_child) == 0:
               return False
            tempNode = matching_child[0]
            tempWord = tempWord[1:]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)