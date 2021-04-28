class Node:
    def __init__(self, data, end):
        self.children = []
        self.data = data
        self.end = end

class Trie:

    def __init__(self):
        self.root = Node("*", False)
        self.words = []

    def get_words(self):
        self.words.clear()
        self.get_words_helper(self.root, "")

    def get_words_helper(self, node, prefix):
        

    def add_word(self, word):

        if self.search(word):
            return

        node = self.root
        chars = list(word)
        for i in range(len(chars)):
            target_char = chars[i]
            found = False
            for child in node.children:
                if child.data == target_char:
                    node = child
                    found = True
            if not found:
                end = False
                if i == len(chars) - 1:
                    end = True
                new_node = Node(target_char, end)
                node.children.append(new_node)
                node = new_node
    
    def search(self, word):
        node = self.root
        chars = list(word)
        for i in range(len(chars)):
            found = False
            target_char = chars[i]
            for child in node.children:
                if child.data == target_char:
                    found = True
                    node = child
            if not found:
                return False
        if node.end:
            return True
        return False



trie = Trie()
trie.add_word("apple")
trie.add_word("apply")
trie.add_word("boat")
trie.add_word("bot")
