class Node:
    def __init__(self, data, is_end):
        self.children = []
        self.end = is_end
        self.data = data

class Trie:

    def __init__(self):
        self.root = Node('*', False)

    def display_client(self):
        self.display(self.root)

    def display(self, node):
        children = node.children
        s = ""
        for i in range(len(children)):
            s += children[i].data
        print(s)

    def add_word(self, word):
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
            if len(node.children) == 0:
                    end = False
                    if i == len(chars) - 1:
                        end = True
                    new_node = Node(target_char, end)
                    node.children.append(new_node)
                    node = new_node



trie = Trie()
trie.add_word("apple")
trie.add_word("car")
trie.add_word("wab")
trie.add_word("ack")
trie.display_client()
