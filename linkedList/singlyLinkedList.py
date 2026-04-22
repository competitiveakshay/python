class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class singlyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    def traversal(self):
        if self.head is None:
            print("SLL is Empty")
        else:
            current = self.head
            while current is not None:
                if current.next is not None:
                    print(current.val, end=" --> ")
                else:
                    print(current.val)
                current = current.next
    
    def insert(self, val, position):
        new_node = Node(val)
        
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        
        else:
            current = self.head
            prev_node = None
            count = 0

            while current is not None and count < position:
                prev_node = current
                current = current.next
                count += 1
            
            prev_node.next = new_node
            new_node.next = current
    
    def delete(self, val):
        temp = self.head
        if temp.val == val:
            self.head = temp.next
            return
        else:
            found = False
            prev = None
            while temp is not None:
                if temp.val == val:
                    found = True
                    break
                prev = temp
                temp = temp.next

            if found:
                prev.next = temp.next
                return
            else:
                print("Node not Found")

    def reverse(self):
        prev = None
        temp = self.head

        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        
        self.head = prev

sll = singlyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)
sll.traversal()

sll.reverse()
sll.traversal()

