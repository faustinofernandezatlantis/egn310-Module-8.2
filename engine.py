import time

# =====================================================================
# 1. CUSTOM DOUBLY LINKED LIST & LRU CACHE (Search History)
# =====================================================================
class LRUNode:
    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """
    O(1) LRU Cache implemented using a Doubly Linked List + Hash Map.
    Provides constant-time lookup, insertion, and eviction for recent searches.
    """
    def __init__(self, capacity: int = 5):
        self.capacity = capacity
        self.cache = {}  # key -> LRUNode
        # Dummy head and tail nodes to eliminate edge-case checks
        self.head = LRUNode("", "")
        self.tail = LRUNode("", "")
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: LRUNode):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node: LRUNode):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: str):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_front(node)
            return node.value
        return None

    def put(self, key: str, value: str):
        if key in self.cache:
            self._remove(self.cache[key])
        elif len(self.cache) >= self.capacity:
            # Evict Least Recently Used (LRU) node (right before tail)
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

        new_node = LRUNode(key, value)
        self._add_to_front(new_node)
        self.cache[key] = new_node

    def get_history(self):
        history = []
        curr = self.head.next
        while curr != self.tail:
            history.append((curr.key, curr.value))
            curr = curr.next
        return history


# =====================================================================
# 2. CUSTOM TRIE (Prefix Tree) WITH TOP-K AUTOCOMPLETE
# =====================================================================
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.frequency = 0


class Trie:
    """
    Prefix Tree (Trie) supporting exact search, insertion, and 
    frequency-ranked Top-K auto-completion.
    """
    def __init__(self):
        self.root = TrieNode()
        self._total_words = 0

    def insert(self, word: str, frequency: int = 1):
        word = word.lower().strip()
        if not word:
            return
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        if not curr.is_end_of_word:
            curr.is_end_of_word = True
            self._total_words += 1
        curr.frequency += frequency

    def search(self, word: str) -> bool:
        word = word.lower().strip()
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end_of_word

    def autocomplete(self, prefix: str, k: int = 5):
        prefix = prefix.lower().strip()
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return []
            curr = curr.children[char]

        results = []
        self._dfs(curr, prefix, results)
        # Sort by frequency descending, then alphabetically ascending
        results.sort(key=lambda x: (-x[1], x[0]))
        return [word for word, freq in results[:k]]

    def _dfs(self, node: TrieNode, current_prefix: str, results: list):
        if node.is_end_of_word:
            results.append((current_prefix, node.frequency))
        for char, child_node in node.children.items():
            self._dfs(child_node, current_prefix + char, results)

    def __len__(self):
        return self._total_words