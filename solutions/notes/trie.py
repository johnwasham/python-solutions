# aka prefix tree

# insert word O(1)
# search word O(1) - since words are short
# search prefix O(1) - autocomplete

# a-z

# empty root node with 26 children
# each child has at most 26 children

# use a hashmap for children, key = a-z

class TrieNode:
    def __init__(self):
        self.children = {}
        self.ends_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.ends_word = True

    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.ends_word

    def prefix(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
