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
        print(node.data)
        for i in range(len(node.children)):
            child = node.children[i]
            print(child.data)
            grandchildren = child.children
            for j in range(len(grandchildren)):
                self.display(grandchildren[j])

    def add_word(self, word):
        chars = list(word)

        for i in range(len(chars)):

            end = False
            if i == len(chars) - 1:
                end = True
            node = Node(chars[i], end)
            
            prefix = []
            j = 0
            while j < i:
                prefix.append(chars[j])
                j += 1

            self.add_char_node(node, prefix)

    def add_char_node(self, node, prefix):
        search_node = self.root
        
        # got the algorithm to add the first character to the trie, we need to use an iterative approach to add the rest of the nodes:
        if len(prefix) == 0:
            add = True
            for i in range(len(search_node.children)):
                if search_node.children[i].data == node.data and search_node.children[i].end == node.end:
                    add = False
                    new_node = search_node.children[i]
                    search_node = new_node
            if add:
                search_node.children.append(node)
                search_node = node

        '''
            Example: apple
            a      []
            ap     [a]
            app    [a, p]
            appl   [a, p, p]
            apple  [a, p, p, l]

            the search node will start at the root, the first line has already been taken care of, a will ba added to the root node if it does not already exist as a child of the root node
            for 'ap', we need to first find a in the root node and create it if it doesn't exist
            for 'ap', we need to find p in the a node above and create it if it doesn't exist
            for 'app', we need to find p in the p node above and create it if it doesn't exist
            for 'appl' we need to find l in the p node above and create it if it doesn't exist
            for 'apple' we need to find e in the l node above and create it if it doesn't exist
        '''




trie = Trie()
trie.add_word("apple")
trie.display_client()
