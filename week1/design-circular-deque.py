class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.size = 0
        self.max_size = k
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.head.prev = self.tail
        self.tail.next = self.head
        self.tail.prev = self.head

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        nodeToInsert = Node(value, prev=self.head, next=self.head.next)
        self.head.next.prev = nodeToInsert
        self.head.next = nodeToInsert
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        nodeToInsert = Node(value, prev=self.tail.prev, next=self.tail)
        self.tail.prev.next = nodeToInsert
        self.tail.prev = nodeToInsert
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        nodeToDelete = self.head.next
        self.head.next = nodeToDelete.next
        nodeToDelete.next.prev = self.head
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        nodeToDelete = self.tail.prev
        self.tail.prev = nodeToDelete.prev
        nodeToDelete.prev.next = self.tail
        self.size -= 1
        return True
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.head.next.value
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.tail.prev.value
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.size == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.size == self.max_size
