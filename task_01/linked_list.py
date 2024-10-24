from __future__ import annotations


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next: Node | None = None

    def to_array(self):
        curr = self
        res = []
        while curr:
            res.append(curr.data)
            curr = curr.next
        return res

    def middle(self) -> Node | None:
        if self is None:
            return None
        slow, fast = self, self
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    @staticmethod
    def merge_sorted(n1: Node, n2: Node) -> Node | None:
        head = Node()
        tail = head
        while n1 and n2:
            if n1.data <= n2.data:
                tail.next, n1 = n1, n1.next
            else:
                tail.next, n2 = n2, n2.next
            tail = tail.next
        if n1:
            tail.next = n1
        elif n2:
            tail.next = n2

        return head.next


class LinkedList:
    def __init__(self):
        self.head: Node | None = None

    def reverse(self):
        it = self.head
        prev = None
        while it:
            cur = it.next
            it.next = prev
            prev = it
            it = cur
        self.head = prev

    def sort(self):
        def split_and_sort(head: Node) -> Node | None:
            if head is None or head.next is None:
                return head

            mid = head.middle()
            high = mid.next
            mid.next = None

            sorted_low = split_and_sort(head)
            sorted_high = split_and_sort(high)

            return Node.merge_sorted(sorted_low, sorted_high)

        self.head = split_and_sort(self.head)

    @staticmethod
    def merge_sorted(list_a: LinkedList, list_b: LinkedList) -> LinkedList:
        if list_a is None:
            return list_b
        if list_b is None:
            return list_a

        list_a.sort()
        list_b.sort()
        res = LinkedList()
        res.head = Node.merge_sorted(list_a.head, list_b.head)
        list_a.head = None
        list_b.head = None
        return res

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        if self.head is None:
            print("[]")
            return
        print("[" + ", ".join([str(d) for d in self.head.to_array()]) + "]")
