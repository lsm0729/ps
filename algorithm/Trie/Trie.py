

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string

    def search(self, string):
        current_node = self.head

        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False

        if current_node.data:
            return True
        else:
            return False

    def starts_with(self, prefix):
        current_node = self.head
        words = []

        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return None

        current_node = [current_node]
        next_node = []
        while True:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break

        return words
    """
    1. head를 빈노드로 설정
    2. insert : 트리 생성. 입력된 문자열의 문자를 하나씩 childern에 확인후 저장하고
                문자열을 다 돌면 마지막 노드의 data에 문자열 저장
    3. search : 문자열이 존재하는지에 대한 여부를 리턴. 문자열을 하나씩 돌면서 확인후
    마지막 노드가 data가 존재한다면 True, 그렇지 않거나 애초에 childern에 존재하지 
    않는다면 False
    
    4. starts_with : prefix단어로 시작하는 단어를 찾고 배열로 리턴.
    prefix단어까지 트리를 순회한후 그다음부터 data가 존재하는 것들만 배열에 저장하여 return
    
    
    """

trie = Trie()
word_list = ["frodo", "front", "firefox", "fire"]
for word in word_list:
    trie.insert(word)

print(trie.search("frodo"))

print(trie.starts_with("fire"))