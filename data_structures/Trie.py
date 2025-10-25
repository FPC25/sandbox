class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_end_of_word = False

class Trie: 
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        current_node = self.root
        
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]

        current_node.is_end_of_word = True
        
    def search(self, word):
        current_node = self.root
        
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        
        return current_node.is_end_of_word
    
    def _delete(self, current_node, word, index):
        if index == len(word):
            if not current_node.is_end_of_word:
                return False  # Word not found
            current_node.is_end_of_word = False
            return len(current_node.children) == 0  # If no children, node can be deleted

        char = word[index]
        node = current_node.children.get(char)
        if node is None:
            return False  # Word not found

        delete_current_node = self._delete(node, word, index + 1)

        if delete_current_node:
            del current_node.children[char]
            return len(current_node.children) == 0 and not current_node.is_end_of_word

        return False
    
    def delete(self, word):
        self._delete(self.root, word, 0)
    
    def has_prefix(self, prefix):
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]

        return True
    
    def starts_with(self, prefix):
        def _dfs(current_node, path):
            if current_node.is_end_of_word:
                words.append(''.join(path))

            for char, child_node in current_node.children.items():
                _dfs(child_node, path + [char])
                
        words = []
        current_node = self.root
        
        for char in prefix:
            if char not in current_node.children:
                return words  # No words with the given prefix
            current_node = current_node.children[char]

        # If we found the prefix, we need to find all words with this prefix
        _dfs(current_node, list(prefix))
        
        return words

    def list_words(self):
        def _dfs(current_node, path):
            if current_node.is_end_of_word:
                words.append(''.join(path))

            for char, child_node in current_node.children.items():
                _dfs(child_node, path + [char])
                
        words = []
        _dfs(self.root, [])
        
        return words
    
    
if __name__ == "__main__":
    
    trie = Trie()
    trie.insert("hello")
    trie.insert("henry")
    trie.insert("helium")
    trie.insert("hero")
    trie.insert("her")
    trie.insert("helicopter")
    trie.insert("mike")
    trie.insert("minimum")
    trie.insert("minimal")
    trie.insert("mini")
    
    print(trie.list_words())          # ['hello', 'henry', 'helium', 'hero', 'her', 'helicopter', 'mike', 'minimum', 'minimal', 'mini']
    
    print(trie.has_prefix("he"))     # True
    print(trie.has_prefix("herm"))   # False    
    print(trie.has_prefix("mi"))     # True
    
    print(trie.starts_with("he"))    # ['hello', 'helium', 'henry', 'hero', 'her', 'helicopter']
    print(trie.starts_with("her"))   # ['hero', 'her']
    print(trie.starts_with("mi"))    # ['mike', 'minimum', 'minimal', 'mini']
    
    trie.delete("hero")
    trie.delete("minimal")

    print(trie.search("hello"))      # True
    print(trie.search("helium"))     # True
    print(trie.search("heroic"))     # False
    print(trie.search("min"))        # False
    print(trie.search("mini"))       # True
    print(trie.search("minimum"))    # True
    print(trie.search("minimal"))    # False
    