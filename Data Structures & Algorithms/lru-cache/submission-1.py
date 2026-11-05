class ListNode:

    def __init__(self, key: int = -1, value: int = -1):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._nodes = {}
        self._head = ListNode()
        self._tail = ListNode()
        self._head.next = self._tail
        self._tail.prev = self._head

    def get(self, key: int) -> int:
        if key not in self._nodes:
            return -1

        node = self._nodes[key]
        self._remove_node(node)
        self._add_to_mru(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self._nodes:
            node = self._nodes[key]
            self._remove_node(node)
            del self._nodes[key]


        new = ListNode(key, value)
        self._nodes[key] = new
        self._add_to_mru(new)

        if len(self._nodes) > self._capacity:
            node = self._head.next
            self._remove_node(node)
            del self._nodes[node.key]




    def _remove_node(self, node: ListNode) -> None:
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _add_to_mru(self, node:ListNode) -> None:
        prev_tail = self._tail.prev
        prev_tail.next = node
        node.next = self._tail
        node.prev = prev_tail
        self._tail.prev = node
        

    """
        example
            LRU cache state: head -> 0 -> 1  -> 2 -> 3 -> tail

            get 0, 
                0.prev.next = 0.next
                    head -> 1  -> 2 -> 3 -> tail
                tail_prev = tail.prev
                tail_prev.next = 0
                0.prev = tail_prev
                0.next = tail
                tail.prev = 0
                result: head -> 1  -> 2 -> 3 -> 0 -> tail
            put 5
                result: head -> 1  -> 2 -> 3 -> 0 -> 5 -> tail
            get 2
                result: head -> 1  -> 3 -> 0 -> 5 -> 2 -> tail


            tail is most recently used side
            head is least recently used


    """