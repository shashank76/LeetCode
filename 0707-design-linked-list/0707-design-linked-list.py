class ListNode:
    def __init__(self, val):
        self.prev = None
        self.val = val
        self.next = None
        
class MyLinkedList:
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left
        
    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index-=1
        if cur and cur != self.right and index == 0:
            return cur.val
        return -1
        

    def addAtHead(self, val: int) -> None:
        node, prevVal, nextVal = ListNode(val), self.left, self.left.next
        prevVal.next = nextVal.prev = node
        node.prev, node.next = prevVal, nextVal        

    def addAtTail(self, val: int) -> None:
        node, prevVal, nextVal = ListNode(val), self.right.prev, self.right
        prevVal.next = nextVal.prev = node
        node.prev, node.next = prevVal, nextVal 
        

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index-=1
        if cur and index == 0:
            node, prevVal, nextVal = ListNode(val), cur.prev, cur
            prevVal.next = nextVal.prev = node
            node.prev, node.next = prevVal, nextVal
        

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index-=1
        if cur and cur != self.right and index == 0:
            prevVal, nextVal = cur.prev, cur.next
            prevVal.next = nextVal
            nextVal.prev = prevVal
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)