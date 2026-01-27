"""
707. Design Linked List

Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.


Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3


Constraints:

0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.
"""


class MyLinkedList:
    head = None
    tail = None

    def __init__(self):
        pass

    def get(self, index: int) -> int:
        curr = self.head
        while curr and index:
            curr = curr.next
            index -= 1

        if curr and index == 0:
            return curr.val

        return -1

    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.tail = self.head = Node(val)
            return

        next = self.head
        self.head = Node(val)
        self.head.next = next

    def addAtTail(self, val: int) -> None:
        if not self.tail:
            self.addAtHead(val)
            return

        new_tail = Node(val)
        self.tail.next = new_tail
        self.tail = new_tail

    def addAtIndex(self, index: int, val: int) -> None:
        if not self.head and index == 0:
            self.addAtHead(val)
            return

        curr = self.head
        while curr and index:
            curr = curr.next
            index -= 1

        if not curr and index == 0: # we went off the end
            self.addAtTail(val)
            return

        if curr and index == 0:
            node = Node(curr.val)
            node.next = curr.next
            if curr.next is None:
                self.tail = node
            curr.next = node
            curr.val = val

    def deleteAtIndex(self, index: int) -> None:
        if self.head and index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            index -= 1
            while curr and index:
                curr = curr.next
                index -= 1
            if curr and curr.next:
                if curr.next == self.tail:
                    self.tail = curr
                curr.next = curr.next.next

    def __str__(self):
        print("start")
        curr = self.head
        while curr:
            print("value:" + str(curr.val))
            curr = curr.next
        print("end")


class Node:
    val = None
    next = None

    def __init__(self, val):
        self.val = val


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(7)
obj.addAtHead(2)
obj.addAtHead(1)
obj.addAtIndex(3, 0)
obj.deleteAtIndex(2)
obj.addAtHead(6)
obj.addAtTail(4)
assert obj.get(4) == 4
obj.addAtHead(4)
obj.addAtIndex(5, 0)
obj.addAtHead(6)
print(obj.__str__())
